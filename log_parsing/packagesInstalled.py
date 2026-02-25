from datetime import datetime

try:
    with open('/var/log/dpkg.log', 'r') as f:
        today = datetime.now().strftime('%Y-%m-%d')
        ls = []
        lines = f.readlines()
        for line in lines:
            words = line.split()
            if 'status installed' in line:
                ls.append({'package': words[-2],
                    'version': words[-1],
                    'date': words[0],
                    'time': words[1]})
            elif words[2] == 'install':
                ls.append({'package': words[3],
                    'version': words[-1],
                    'date': words[0],
                    'time': words[1]})
    print(sorted(ls, key=lambda x: x['date'] + x['time']))

except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    print(e)