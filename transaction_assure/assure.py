import sqlite3

def create_conn(filepath='transaction_assure/assure.db'):
    return sqlite3.connect(filepath)

def create_db(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assure (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            plafond INTEGER,
            total_rembourse INTEGER,
            status TEXT NOT NULL
        )
    """)
    conn.commit()

def insert_assure(conn, assure):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT into assure (nom, plafond, total_rembourse, status)
        VALUES (?, ?, ?, ?)
    """, (assure['nom'], assure['plafond'], assure['total_rembourse'], assure['status']))

    conn.commit()


def get_assure_ceil(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assure WHERE plafond < total_rembourse")
    return cursor.fetchall()


def update_status(conn, id):
    cursor = conn.cursor()
    cursor.execute("UPDATE assure SET status = ? WHERE id = ?", ("plafonne", id))
    conn.commit()


if __name__ == '__main__':
    conn = create_conn()
    create_db(conn)
    insert_assure(conn, {'nom': "Sean", 'plafond': 9000, 'total_rembourse': 1000, 'status': "actif"})
    ceil = get_assure_ceil(conn)
    for assure in ceil:
        update_status(conn, assure[0])

    conn.close()
