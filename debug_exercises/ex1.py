import json
import sqlite3

def load_remboursements(filepath):
    with open(filepath, 'w') as f:
        return json.load(f)

def get_patient(conn, patient_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = ?", patient_id)
    return cursor.fetchone()

def calculer_total(remboursements):
    total = 0
    for r in remboursements:
        total += r['montant']
    return total

def sauvegarder_total(conn, patient_id, total):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE patients SET total = total + ? WHERE id = ?",
        (patient_id, total)
    )
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('patients.db')
    data = load_remboursements('remboursements.json')
    for patient_id in [1, 2, 3]:
        patient = get_patient(conn, patient_id)
        remboursements_patient = [r for r in data if r['patient_id'] == patient_id]
        total = calculer_total(remboursements_patient)
        sauvegarder_total(conn, patient_id, total)
    conn.close()