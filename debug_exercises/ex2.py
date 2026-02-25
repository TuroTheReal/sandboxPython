import json
import sqlite3
from datetime import datetime

def load_transactions(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def filtrer_transactions_recentes(transactions, jours=30):
    aujourd_hui = datetime.now()
    recentes = []
    for t in transactions:
        date_transaction = datetime.strptime(t['date'], '%Y-%m-%d')
        delta = aujourd_hui - date_transaction
        if delta.days <= jours:
            recentes.append(t)
    return recentes

def calculer_stats(transactions):
    if len(transactions) == 0:
        return None
    total = sum(t['montant'] for t in transactions)
    moyenne = total / len(transactions)
    maximum = max(t['montant'] for t in transactions)
    return {'total': total, 'moyenne': moyenne, 'maximum': maximum}

def sauvegarder_stats(conn, patient_id, stats):
    if stats == None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO stats (patient_id, total, moyenne, maximum, date_calcul)
        VALUES (?, ?, ?, ?, ?)
    """, (patient_id, stats['total'], stats['moyenne'], stats['maximum'], datetime.now()))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('stats.db')
    data = load_transactions('transactions.json')
    for patient_id in [1, 2, 3]:
        transactions_patient = [t for t in data if t['patient_id'] == patient_id]
        recentes = filtrer_transactions_recentes(transactions_patient)
        stats = calculer_stats(recentes)
        sauvegarder_stats(conn, patient_id, stats)
    conn.close()