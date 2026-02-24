import json

def extract_json(filepath='transaction_assure/transaction.txt'):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def get_categories(data):
    return {obj['categorie'] for obj in data}


def calcul_categories(data, category):
    total = 0
    for obj in data:
        if obj['categorie'] == category:
            total += obj['montant']
    return total


def create_report(data):
    report = {}
    categories = get_categories(data)

    for category in categories:
        total = calcul_categories(data, category)
        report[category] = total

    return report


def write_json(report, filepath='transaction_assure/transaction_report.json'):
    with open(filepath, 'w') as f:
        json.dump(report, f, indent=2)


if __name__ == '__main__':
    data = extract_json()
    report = create_report(data)
    write_json(report)
