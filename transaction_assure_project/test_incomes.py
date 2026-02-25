import pytest
import sqlite3
from assure import create_conn, create_db, insert_assure
from incomes import check_id_exists, update_total_rembourse, log_erreur


@pytest.fixture
def db(tmp_path):
    conn = create_conn(tmp_path / "test.db")
    create_db(conn)
    insert_assure(conn, {'nom': 'Sean', 'plafond': 9000, 'total_rembourse': 0, 'status': 'actif'})
    insert_assure(conn, {'nom': 'Paul', 'plafond': 5000, 'total_rembourse': 0, 'status': 'actif'})
    return conn


def test_check_id_exists_trouve(db):
    assert check_id_exists(db, 1) is True

def test_check_id_exists_inconnu(db):
    assert check_id_exists(db, 99) is False


def test_update_total_rembourse_ajoute_montant(db):
    update_total_rembourse(db, 1, 100)
    cursor = db.cursor()
    cursor.execute("SELECT total_rembourse FROM assure WHERE id = 1")
    assert cursor.fetchone()[0] == 100

def test_update_total_rembourse_additionne(db):
    update_total_rembourse(db, 1, 100)
    update_total_rembourse(db, 1, 50)
    cursor = db.cursor()
    cursor.execute("SELECT total_rembourse FROM assure WHERE id = 1")
    assert cursor.fetchone()[0] == 150


def test_log_erreur_cree_fichier(tmp_path):
    filepath = tmp_path / "erreurs.txt"
    log_erreur(99, filepath)
    assert filepath.exists()

def test_log_erreur_contenu(tmp_path):
    filepath = tmp_path / "erreurs.txt"
    log_erreur(99, filepath)
    assert "99" in filepath.read_text()

def test_log_erreur_append(tmp_path):
    filepath = tmp_path / "erreurs.txt"
    log_erreur(11, filepath)
    log_erreur(99, filepath)
    contenu = filepath.read_text()
    assert "11" in contenu
    assert "99" in contenu