import pytest
import sqlite3
from assure import get_assure_ceil, insert_assure, create_conn, create_db, update_status

@pytest.fixture
def db(tmp_path):
    conn = create_conn(tmp_path / "test.db")

    create_db(conn)

    insert_assure(conn, {'nom': 'Arthur', 'plafond': 1000, 'total_rembourse': 1500, 'status': 'actif'})
    insert_assure(conn, {'nom': 'Paul', 'plafond': 2000, 'total_rembourse': 500, 'status': 'actif'})

    return conn


def test_create_conn_retourne_connexion(tmp_path):
    conn = create_conn(tmp_path / "test.db")
    assert isinstance(conn, sqlite3.Connection)
    assert conn is not None

def test_create_db_table_existe(db):
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='assure'")
    assert cursor.fetchone() is not None

def test_create_db_colonnes_correctes(db):
    cursor = db.cursor()

    cursor.execute("PRAGMA table_info('assure')")
    colonne = [row[1] for row in cursor.fetchall()]
    assert colonne == ['id', 'nom', 'plafond', 'total_rembourse', 'status']

def test_insert_assure_present_en_db(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT (*) FROM assure")
    before = cursor.fetchone()[0]
    insert_assure(db,  {'nom': "Bob", 'plafond': 10000, 'total_rembourse': 9999, 'status': "inactif"})
    cursor.execute("SELECT COUNT (*) FROM assure")
    after = cursor.fetchone()[0]
    assert after == before + 1

def test_insert_assure_valeurs_correctes(db):
    cursor = db.cursor()
    insert_assure(db,  {'nom': "Bob", 'plafond': 10000, 'total_rembourse': 9999, 'status': "inactif"})
    cursor.execute("SELECT * FROM assure WHERE nom = 'Bob'")
    row = cursor.fetchone()
    assert row[1] == 'Bob'
    assert row[2] == 10000
    assert row[3] == 9999
    assert row[4] == 'inactif'

def test_get_assure_ceil_retourne_liste(db):
    assert isinstance(get_assure_ceil(db), list)

def test_get_assure_ceil_depasse(db):
    result = get_assure_ceil(db)
    assert len(result) == 1
    assert result[0][1] == 'Arthur'

def test_get_assure_ceil_aucun_depasse(tmp_path):
    conn = create_conn(tmp_path / "test.db")
    create_db(conn)
    insert_assure(conn, {'nom': 'Paul', 'plafond': 2000, 'total_rembourse': 500, 'status': 'actif'})
    assert get_assure_ceil(conn) == []


def test_update_status_commit_persiste(tmp_path):
    path = tmp_path / "test.db"
    conn = create_conn(path)
    create_db(conn)
    insert_assure(conn, {'nom': 'Paul', 'plafond': 2000, 'total_rembourse': 500, 'status': 'actif'})

    update_status(conn, 1)
    conn.close()

    conn2 = create_conn(path)
    cursor = conn2.cursor()
    cursor.execute("SELECT status FROM assure WHERE id = 1")
    assert cursor.fetchone()[0] == 'plafonne'

def test_update_status_valeur_correcte(db):
    cursor = db.cursor()
    result = get_assure_ceil(db)
    update_status(db, result[0][0])
    cursor.execute("SELECT * FROM assure WHERE nom = 'Arthur'")
    assert cursor.fetchone()[4] == 'plafonne'
