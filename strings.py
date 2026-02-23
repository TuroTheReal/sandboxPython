"""
Exercice 2: Validation et parsing strings
Contexte: Valider format données emails
"""

# TODO 1: Valider format email
def is_valid_email(email):
    """
    Valide format email basique.

    Rules:
    - Doit contenir exactement un @
    - Partie après @ doit contenir au moins un .

    Return: True si valide, False sinon

    Examples:
    - 'alice@gmail.com' → True
    - 'bob@yahoo.co.uk' → True
    - 'invalid-email' → False (pas de @)
    - 'test@@example.com' → False (deux @)
    - 'user@domain' → False (pas de . après @)
    """

    if '@' not in email:
        return False

    words = email.split('@')
    if len(words) != 2:
        return False

    if '.' not in words[1]:
        return False

    return True

# TODO 2: Extraire domaine d'email
def get_domain(email):
    """
    Extrait le domaine d'un email.

    Return: domaine (str) ou None si email invalide

    Examples:
    - 'alice@gmail.com' → 'gmail.com'
    - 'bob@company.co.uk' → 'company.co.uk'
    - 'invalid-email' → None
    """
    if is_valid_email(email):
        words = email.split('@')
        return words[1]
    else:
        return None


# TODO 3: Grouper emails par domaine
def group_by_domain(emails):
    """
    Groupe une liste d'emails par domaine.

    Return: dict avec domaine comme key, liste emails comme value
    Ignore les emails invalides

    Example:
    Input: ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 'invalid']
    Output: {
        'gmail.com': ['alice@gmail.com', 'charlie@gmail.com'],
        'yahoo.com': ['bob@yahoo.com']
    }
    """
    group = {}

    for email in emails:
        domain = get_domain(email)
        if domain:
            if domain not in group:
                group[domain] = []
            group[domain].append(email)
    return group

# Tests
if __name__ == "__main__":
    # Test 1: Validation
    print("=" * 30)
    print("TEST 1: Validation emails")
    print("=" * 30)
    test_emails = [
        'alice@gmail.com',
        'bob@yahoo.com',
        'charlie@gmail.com',
        'invalid-email',
        'test@@example.com',
        'user@domain',
        'good@company.co.uk'
    ]

    for email in test_emails:
        valid = is_valid_email(email)
        status = "✅" if valid else "❌"
        print(f"  {status} {email}")
    print()

    # Test 2: Extraction domaine
    print("=" * 30)
    print("TEST 2: Extraction domaines")
    print("=" * 30)
    for email in test_emails:
        domain = get_domain(email)
        if domain:
            print(f"  📧 {email:25} → {domain}")
        else:
            print(f"  ❌ {email:25} → Invalid")
    print()

    # Test 3: Groupement
    print("=" * 30)
    print("TEST 3: Groupement par domaine")
    print("=" * 30)
    grouped = group_by_domain(test_emails)
    for domain, emails in grouped.items():
        print(f"  📊 {domain}:")
        for email in emails:
            print(f"      - {email}")
    print()