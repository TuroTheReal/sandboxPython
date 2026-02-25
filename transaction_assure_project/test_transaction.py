import pytest, json
from transaction import calcul_categories, create_report, get_categories, write_json, extract_json

@pytest.fixture
def transactions():
    return [
        {"id": "p2", "date": "2024-01-18", "montant": 120.00, "categorie": "dentaire"},
        {"id": "p1", "date": "2024-02-01", "montant": 80.00, "categorie": "optique"},
        {"id": "p1", "date": "2024-02-01", "montant": 16.00, "categorie": "optique"},
        {"id": "p3", "date": "2024-02-10", "montant": 30.00, "categorie": "medecin"},
        {"id": "p1", "montant": -45.50, "categorie": "medecin"},
        {"id": "p3", "montant": -10.00, "categorie": "medecin"},
        {"id": "p2", "montant": -92.00, "categorie": "dentaire"},
    ]

def test_calcul_categories_normal(transactions):
    assert calcul_categories(transactions, "optique") == 96.00

def test_calcul_categories_not_exists(transactions):
    assert calcul_categories(transactions, "jean") == 0

def test_calcul_categories_negatif(transactions):
    assert calcul_categories(transactions, "medecin") == -25.50



def test_create_report_dict(transactions):
    assert create_report(transactions) == {'dentaire': 28.0, 'medecin': -25.5, 'optique': 96.0}

def test_create_report_all_categories_find(transactions):
    report = create_report(transactions)
    assert len(report) == 3

def test_create_report_empty():
    assert create_report([]) == {}



def test_write_created(tmp_path, transactions):
    files = tmp_path / "test_transaction_report.json"
    write_json(transactions, files)
    assert files.exists()

def test_write_correct_files(tmp_path, transactions):
    result = {"optique": 96.0, "dentaire": 28.0, "medecin": -25.5}
    files = tmp_path / "test_transaction_report.json"
    write_json(create_report(transactions), files)
    assert extract_json(files) == result



def test_extract_normal(tmp_path):
    files = tmp_path / "transaction.txt"
    data_input = [
        {"id": "p1", "date": "2024-01-15", "montant": 45.50, "categorie": "medecin"},
        {"id": "p2", "date": "2024-01-18", "montant": 120.00, "categorie": "dentaire"},
        {"id": "p1", "date": "2024-02-01", "montant": 80.00, "categorie": "optique"},
        {"id": "p3", "date": "2024-02-10", "montant": 30.00, "categorie": "medecin"},
        {"id": "p2", "date": "2024-03-05", "montant": 200.00, "categorie": "dentaire"}
    ]
    with open(files, 'w') as f:
        json.dump(data_input, f)
    assert extract_json(files) == data_input

def test_extract_empty(tmp_path):
    files = tmp_path / "transaction.txt"
    files.write_text("[]")
    data = extract_json(files)
    assert data == []



def test_get_categories_normal(transactions):
    assert len(get_categories(transactions)) == 3
def test_get_categories_empty():
    assert get_categories([]) == set()
