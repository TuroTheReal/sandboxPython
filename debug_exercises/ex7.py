import json
import sqlite3
from datetime import datetime

def load_employes(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def calculer_salaire_net(employe):
    brut = employe['salaire_brut']
    taux_imposition = employe['taux_imposition']
    deductions = employe['deductions']
    net = brut - (brut * taux_imposition) - deductions
    return net

def inserer_employe(conn, employe, salaire_net):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employes (id, nom, salaire_brut, salaire_net, departement)
        VALUES (?, ?, ?, ?, ?)
    """, (employe['id'], employe['nom'], employe['salaire_brut'], salaire_net, employe['departement']))
    conn.commit()

def get_employes_departement(conn, departement):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM employes WHERE departement = ?",
        (departement,)
    )
    return cursor.fetchall()

def calculer_masse_salariale(conn, departement):
    employes = get_employes_departement(conn, departement)
    if len(employes) == 0:
        return 0
    total = sum(e[3] for e in employes)
    return total

def trouver_employe_mieux_paye(conn, departement):
    employes = get_employes_departement(conn, departement)
    if not employes:
        return None
    max_salaire = 0
    meilleur = None
    for e in employes:
        if e[3] > max_salaire:
            max_salaire = e[3]
            meilleur = e
    return meilleur

def generer_rapport_departements(conn, departements):
    rapport = []
    for dept in departements:
        masse = calculer_masse_salariale(conn, dept)
        meilleur = trouver_employe_mieux_paye(conn, dept)
        rapport.append({
            'departement': dept,
            'masse_salariale': masse,
            'employe_mieux_paye': meilleur[1] if meilleur else None
        })
    with open('rapport_salaires.json', 'w') as f:
        json.dump(rapport, f)
    return rapport

if __name__ == '__main__':
    conn = sqlite3.connect('rh.db')
    employes = load_employes('employes.json')
    departements = set()
    for employe in employes:
        salaire_net = calculer_salaire_net(employe)
        inserer_employe(conn, employe, salaire_net)
        departements.add(employe['departement'])
    rapport = generer_rapport_departements(conn, departements)
    print(rapport)
    conn.close()