import sqlite3

def create_conn(filepath='assure.db'):
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
    pass

def update_status(conn):
    pass


if __name__ == '__main__':
    conn = create_conn()
    create_db(conn)
    insert_assure(conn, {'nom': "Arthur", 'plafond': 1000000, 'total_rembourse': 75000, 'status': "roue libre"})
