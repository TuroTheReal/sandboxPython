import json
import sqlite3
from datetime import datetime

def load_commandes(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def valider_commande(commande):
    champs_requis = ['id', 'client_id', 'produits', 'date']
    for champ in champs_requis:
        if champ not in commande:
            return False
    if len(commande['produits']) == 0:
        return False
    return True

def calculer_total_commande(commande):
    total = 0
    for produit in commande['produits']:
        total += produit['prix'] * produit['quantite']
    return total

def inserer_commande(conn, commande, total):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO commandes (id, client_id, total, date, statut)
        VALUES (?, ?, ?, ?, ?)
    """, (commande['id'], commande['client_id'], total, commande['date'], 'en_attente'))

def get_commandes_client(conn, client_id):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM commandes WHERE client_id = ?",
        (client_id)
    )
    return cursor.fetchall()

def calculer_total_client(conn, client_id):
    commandes = get_commandes_client(conn, client_id)
    totaux = [c[2] for c in commandes]
    return sum(totaux)

def generer_rapport_clients(conn, client_ids):
    rapport = {}
    for client_id in client_ids:
        total = calculer_total_client(conn, client_id)
        rapport[client_id] = {
            'total_depense': total,
            'actif': total > 0
        }
    return rapport

if __name__ == '__main__':
    conn = sqlite3.connect('commandes.db')
    commandes = load_commandes('commandes.json')
    clients_traites = []
    for commande in commandes:
        if valider_commande(commande):
            total = calculer_total_commande(commande)
            inserer_commande(conn, commande, total)
            if commande['client_id'] not in clients_traites:
                clients_traites.append(commande['client_id'])
    rapport = generer_rapport_clients(conn, clients_traites)
    print(rapport)
    conn.close()