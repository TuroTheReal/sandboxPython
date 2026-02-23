import requests

urls = [
    'https://api.github.com',
    'https://google.com',
    'https://thissitedoesnotexist12345.com'
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is UP")
        else:
            print(f"{url} response is :{response.status_code}")
    except Exception as e:
        print(f"{url} is DOWN - {e}")
    
