import json
import sqlite3

def load_patients(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def get_remboursements(conn, patient_id):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT montant FROM remboursements WHERE patient_id = ?",
        (patient_id,)
    )
    return cursor.fetchall()

def calculer_total(remboursements):
    total = 0
    for r in remboursements:
        total += r
    return total

def verifier_plafond(total, plafond):
    return total > plafond

def mettre_a_jour_statut(conn, patient_id, statut):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE patients SET statut = ? WHERE id = ?",
        (statut, patient_id)
    )

def generer_rapport(patients, resultats):
    rapport = []
    for i in range(len(patients)):
        rapport.append({
            'nom': patients[i]['nom'],
            'total': resultats[i]['total'],
            'statut': resultats[i]['statut']
        })
    return rapport

def sauvegarder_rapport(rapport, filepath):
    with open(filepath, 'w') as f:
        json.dump(rapport, f)

if __name__ == '__main__':
    conn = sqlite3.connect('patients.db')
    patients = load_patients('patients.json')
    resultats = []
    for patient in patients:
        remboursements = get_remboursements(conn, patient['id'])
        total = calculer_total(remboursements)
        depasse = verifier_plafond(total, patient['plafond'])
        if depasse:
            mettre_a_jour_statut(conn, patient['id'], 'plafonné')
        resultats.append({'total': total, 'statut': 'plafonné' if depasse else 'actif'})
    rapport = generer_rapport(patients, resultats)
    sauvegarder_rapport(rapport, 'rapport.json')
    conn.close()