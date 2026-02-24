import json

def read_files():
    with open('nginx.log', 'r') as f:
        return f.readlines()

def normalize_errors(errors):
    report = []
    for (method, endpoint), count in errors.items():
        report.append({
            'method' : method,
            'endpoint' : endpoint,
            'error_count': count
        })
    report.sort(key=lambda x: x['error_count'], reverse=True)
    return report[:3]

def analyze_data(data):
    total = 0
    count2xx = 0
    count4xx = 0
    count5xx = 0
    errors = {}

    for line in data:
        total += 1

        word = line.split()

        status = int(word[-2])

        if 200 <= status < 300:
            count2xx += 1
        if 400 <= status < 500:
            count4xx += 1
        if 500 <= status < 600:
            count5xx += 1

        if status >= 400:
            key = (word[-5][1:], word[-4])
            if key not in errors:
                errors[key] = 0
            errors[key] += 1

    return {
        'total': total,
        'count_2xx': count2xx,
        'count_4xx': count4xx,
        'count_5xx': count5xx,
        'error_rate': round(((count4xx + count5xx) / total * 100)),
        'error_endpoints': normalize_errors(errors)
    }


if __name__ == '__main__':
    data = read_files()
    report = analyze_data(data)
    print(report)

    with open('nginx_report.json', 'w') as f:
        json.dump(report, f, indent=2)

    print("✅ Rapport généré : nginx_report.json")