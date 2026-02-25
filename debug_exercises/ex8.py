import json
import sqlite3
from datetime import datetime

def load_tickets(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def calculer_priorite(ticket):
    score = 0
    if ticket['type'] == 'bug':
        score += 10
    if ticket['type'] == 'feature':
        score += 5
    if ticket['severite'] == 'critical':
        score += 20
    if ticket['severite'] == 'high':
        score += 10
    if ticket['severite'] == 'low':
        score += 2
    return score

def trier_tickets(tickets):
    return sorted(tickets, key=lambda t: calculer_priorite(t))

def inserer_ticket(conn, ticket, priorite):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tickets (id, titre, type, severite, priorite, statut, date_creation)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (ticket['id'], ticket['titre'], ticket['type'], ticket['severite'], priorite, 'ouvert', datetime.now()))
    conn.commit()

def get_tickets_critiques(conn):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM tickets WHERE severite = 'critical' AND statut = 'ouvert'"
    )
    return cursor.fetchall()

def cloturer_ticket(conn, ticket_id):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tickets SET statut = 'cloture' WHERE id = ?",
        (ticket_id)
    )
    conn.commit()

def generer_stats(tickets):
    if not tickets:
        return {}
    stats = {
        'total': len(tickets),
        'par_type': {},
        'par_severite': {},
        'priorite_moyenne': sum(t['priorite'] for t in tickets) / len(tickets)
    }
    for ticket in tickets:
        type_ticket = ticket['type']
        severite = ticket['severite']
        if type_ticket not in stats['par_type']:
            stats['par_type'][type_ticket] = 0
        stats['par_type'][type_ticket] += 1
        if severite not in stats['par_severite']:
            stats['par_severite'][severite] = 0
        stats['par_severite'][severite] += 1
    return stats

if __name__ == '__main__':
    conn = sqlite3.connect('tickets.db')
    tickets = load_tickets('tickets.json')
    tickets_tries = trier_tickets(tickets)
    for ticket in tickets_tries:
        priorite = calculer_priorite(ticket)
        inserer_ticket(conn, ticket, priorite)
    critiques = get_tickets_critiques(conn)
    stats = generer_stats(tickets)
    print(f"Total tickets: {stats['total']}")
    print(f"Critiques en cours: {len(critiques)}")
    conn.close()