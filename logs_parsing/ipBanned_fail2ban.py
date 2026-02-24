try:
    with open('/var/log/fail2ban.log.1', 'r') as f:
        ls = {}
        seen = {'ban': 0, 'unban': 0}
        read = f.readlines()
        for line in read:
            strings = line.split()
            if 'NOTICE' in line:
                if strings[-2] == 'Ban':
                    seen['ban'] += 1
                    ls[strings[-1]] = ls.get(strings[-1], 0) + 1
                elif strings[-2] == 'Unban':
                    seen['unban'] += 1
                    ls[strings[-1]] = ls.get(strings[-1], 0) - 1

    still_banned = {ip: count for ip, count in ls.items() if count > 0}
    print(still_banned)
    print(seen)

except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    print(e)