import requests
import sqlite3

def format_stars(stars):
    """Formate le nombre de stars (1000+ → K)"""

    if stars >= 1000:
        return f"{stars / 1000:.1f}K"
    else:
        return str(stars)

def display_db(conn):
    """Affiche la DB par ordre de stars par repo"""

    cursor = conn.cursor()

    cursor.execute("SELECT id, name, language, stars FROM repos ORDER BY stars DESC LIMIT 10")

    result = cursor.fetchall()

    for repo in result:
        repo_id, name, lang, stars = repo
        print(f"{format_stars(stars):6} ⭐      repo id:{repo_id:3}.  {name:18}  {lang} ")

def fetch_api():
    """Recupere les infos des 30 premiers repos kubernetes"""

    url = 'https://api.github.com/orgs/kubernetes/repos?per_page=30'

    response = requests.get(url, timeout=10)
    if 200 <= response.status_code < 300:
        return response.json()

def create_db(conn):
    """Creer la db si necessaire"""

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS repos")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            language TEXT,
            category TEXT,
            stars INTEGER,
            url TEXT,
            description TEXT
        )
    """)
    conn.commit()

def store_data(repos, conn):
    """Prends les donnees de l'API et creer des tables dans la DB avec ces donnees"""

    cursor = conn.cursor()

    for repo in repos:
        cursor.execute("""
            INSERT INTO repos (name, language, stars, url, description)
            VALUES (?, ?, ?, ?, ?)
        """, (repo['name'], repo['language'], repo['stargazers_count'], repo['html_url'], repo['description']))
    conn.commit()


def enrich_db(conn):
    """generate category based on language

    Args:
        conn (_type_): current db conection
    """
    cursor = conn.cursor()

    cursor.execute("UPDATE repos SET category = 'Backend' WHERE language = 'Go'")
    cursor.execute("UPDATE repos SET category = 'Scripting' WHERE language = 'Python'")
    cursor.execute("UPDATE repos SET category = 'Frontend' WHERE language IN ('JavaScript', 'TypeScript')")
    cursor.execute("UPDATE repos SET category = 'DevOps' WHERE language = 'Shell'")
    cursor.execute("UPDATE repos SET category = 'Other' WHERE category IS NULL")
    conn.commit()

def clean_db(conn, min_stars):
    """enlve les repos stars < min_stars

    Args:
        conn (_type_): current db conection
        min_stars (_type_): nb mini detoiles
    """
    cursor = conn.cursor()

    cursor.execute("DELETE FROM repos WHERE stars < ? ", (min_stars,))
    deleted = cursor.rowcount  # Nombre de lignes supprimées
    print(f"🗑️  Supprimé {deleted} repos")
    conn.commit()

if __name__ == '__main__':

    conn = sqlite3.connect('fromGitToSQLlite.db')

    repos = fetch_api()
    create_db(conn)
    store_data(repos, conn)
    enrich_db(conn)
    clean_db(conn, 9000)
    display_db(conn)

    conn.close()
