from assure import create_conn, insert_assure, get_assure_ceil, update_status
from transaction import extract_json

def check_id_exists(conn, patient_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assure WHERE id = ?", (patient_id,))
    result = cursor.fetchone()
    return result is not None

def update_total_rembourse(conn, patient_id, montant):
    cursor = conn.cursor()
    cursor.execute("UPDATE assure SET total_rembourse = total_rembourse + ? WHERE id = ?", (montant, patient_id))
    conn.commit()

def log_erreur(patient_id, filepath='transaction_assure/errors.txt'):
    with open(filepath, 'a') as f:
        f.write(f"ID inconnu: {patient_id}\n")

if __name__ == '__main__':
    data = extract_json()
    conn = create_conn()

    for line in data:
        if check_id_exists(conn, line['id']):
            update_total_rembourse(conn, line['id'], line['montant'])
        else:
            log_erreur(line['id'])

    ceil = get_assure_ceil(conn)
    for assure in ceil:
        update_status(conn, assure[0])

    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM assure")
    # for row in cursor.fetchall():
    #     print(row)

    conn.close()
