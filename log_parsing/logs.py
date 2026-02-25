def read_files():
    with open('logs.txt', 'r') as f:
        lines = f.readlines()
    return lines

def get_most_freq_error(errors):
    maxi = 0
    max_message = None
    for message, count in errors.items():
        if count > maxi:
            maxi = count
            max_message = message
    return max_message

def analyze_data(data):
    count = 0
    error = 0
    error_type = {}
    most_freq_error = []
    for line in data:
        count += 1
        words = line.split()
        if 'ERROR' == words[2]:
            error += 1
            message = ' '.join(words[3:])
            error_type[message] = error_type.get(message, 0) + 1

    return {
        'total_lines': count,
        'total_error': error,
        'error_breakdown': error_type,
        'most_freq_error': get_most_freq_error(error_type)
    }

def print_report(report):

    print('=' * 20)
    print("LOG ANALYSIS REPORT")
    print('=' * 20)

    for line, count in report.items():
        if 'error_breakdown' == line:
            print(f"  {line}:")
            for error_name, error_count in count.items():
                print(f"      -  {error_name}:  {error_count}")
        else:
            print(f"  {line}:  {count}")

if __name__ == "__main__":

    data = read_files()
    report = analyze_data(data)
    print_report(report)