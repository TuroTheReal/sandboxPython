import json
import re
from datetime import datetime

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

def parse_log_line(line):
    parts = line.split(' ')
    timestamp = parts[0]
    level = parts[1]
    message = ' '.join(parts[2:])
    return {
        'timestamp': timestamp,
        'level': level,
        'message': message
    }

def filter_by_level(logs, level):
    if level not in LOG_LEVELS:
        return []
    return [log for log in logs if log['level'] == level]

def compter_par_level(logs):
    compteur = {}
    for log in logs:
        level = log['level']
        if level in compteur:
            compteur[level] += 1
        else:
            compteur[level] = 1
    return compteur

def sauvegarder_rapport(logs, filepath):
    rapport = {
        'total': len(logs),
        'par_level': compter_par_level(logs),
        'logs': logs
    }
    with open(filepath, 'w') as f:
        json.dump(rapport, f)

if __name__ == '__main__':
    with open('server.log', 'r') as f:
        lines = f.readlines()

    logs = []
    for line in lines:
        log = parse_log_line(line)
        logs.append(log)

    errors = filter_by_level(logs, 'error')
    sauvegarder_rapport(errors, 'rapport_errors.json')