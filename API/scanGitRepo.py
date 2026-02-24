import sys
import requests

def parse(url):
    words = url.split('/')
    repo = words[-1]
    owner = words[-2]
    if 'github.com' in url:
        platform = 'github'
    elif 'gitlab.com' in url:
        platform = 'gitlab'
    else:
        print(f"Platform not supported : {url}")
        sys.exit(1)
    return platform, owner, repo

def fetch(platform, owner, repo):
    if platform == "github":
        url = f"https://api.github.com/repos/{owner}/{repo}"
    else:
        url = f"https://gitlab.com/api/v4/projects/{owner}%2F{repo}"

    try:
        return platform, requests.get(url, timeout=5).json()

    except Exception as e:
        print(e)

def analyze(platform, data):
    if platform == 'github':
        return { 'full' : data.get('full_name', 'Name not found'),
            'stars' : data.get('stargazers_count', 'Not starred yet'),
            'fork' : data.get('forks_count', 'Only 1 fork'),
            'language' : data.get('language', 'N/A'),
            'last_update' : data.get('updated_at', 'Never update since creation'),
            'description' : data.get('description', 'No description')
        }
    elif platform == 'gitlab':
        return { 'full' : data.get('name_with_namespace', 'Name not found').replace(' / ', '/'),
                'stars' : data.get('star_count', 'Not starred yet'),
                'fork' : data.get('forks_count', 'Only 1 fork'),
                'language' : data.get('language', 'N/A'),
                'last_update' : data.get('last_activity_at', 'Never update since creation'),
                'description' : data.get('description', 'No description')
        }
    else:
        print(f"Platform not supported : {platform}")
        sys.exit(1)

def display(info):
    print(f"================ {info['full']} ================")
    print(f"Stars:          {info['stars']}")
    print(f"Fork:           {info['fork']}")
    print(f"Language:       {info['language']}")
    print(f"Last update:    {info['last_update']}")
    print(f"Description:    {info['description']}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python .py <repopath>")
        sys.exit(1)

arg = sys.argv[1]
infos = parse(arg)
data = fetch(*infos)
info = analyze(*data)
display(info)
