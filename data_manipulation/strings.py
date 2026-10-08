"""
Exercise 2: string validation and parsing
Context: validate the format of email data
"""

# TODO 1: Validate email format
def is_valid_email(email):
    """
    Validate a basic email format.

    Rules:
    - Must contain exactly one @
    - The part after @ must contain at least one .

    Return: True if valid, False otherwise

    Examples:
    - 'alice@gmail.com' → True
    - 'bob@yahoo.co.uk' → True
    - 'invalid-email' → False (no @)
    - 'test@@example.com' → False (two @)
    - 'user@domain' → False (no . after @)
    """

    if '@' not in email:
        return False

    words = email.split('@')
    if len(words) != 2:
        return False

    if '.' not in words[1]:
        return False

    return True

# TODO 2: Extract the domain of an email
def get_domain(email):
    """
    Extract the domain of an email.

    Return: domain (str) or None if the email is invalid

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


# TODO 3: Group emails by domain
def group_by_domain(emails):
    """
    Group a list of emails by domain.

    Return: dict with domain as key, list of emails as value
    Ignore invalid emails

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
    print("TEST 1: Email validation")
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

    # Test 2: Domain extraction
    print("=" * 30)
    print("TEST 2: Domain extraction")
    print("=" * 30)
    for email in test_emails:
        domain = get_domain(email)
        if domain:
            print(f"  📧 {email:25} → {domain}")
        else:
            print(f"  ❌ {email:25} → Invalid")
    print()

    # Test 3: Grouping
    print("=" * 30)
    print("TEST 3: Grouping by domain")
    print("=" * 30)
    grouped = group_by_domain(test_emails)
    for domain, emails in grouped.items():
        print(f"  📊 {domain}:")
        for email in emails:
            print(f"      - {email}")
    print()