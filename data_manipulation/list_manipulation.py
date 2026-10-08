"""
Exercise 1: basic list and dict manipulation
Context: you have user data to filter
"""

# Data
users = [
    {'name': 'Alice', 'age': 25, 'active': True, 'role': 'admin'},
    {'name': 'Bob', 'age': 7, 'active': True, 'role': 'user'},
    {'name': 'Charlie', 'age': 30, 'active': False, 'role': 'user'},
    {'name': 'Diana', 'age': 22, 'active': True, 'role': 'admin'},
    {'name': 'Eve', 'age': 19, 'active': False, 'role': 'user'}
]

# TODO 1: Filter users who are active AND adults (>= 18)
def get_active_adults(users):
    active_adults = []
    for user in users:
        if user['active'] and user['age'] >= 18:
            active_adults.append(user)
    return active_adults

# TODO 2: Count users per role
def count_by_role(users):
    count = {}
    for user in users:
        count[user['role']] = count.get(user['role'], 0) + 1
    return count

# TODO 3: Find the youngest active user
def youngest_active(users):
    youngest = None
    for user in users:
        if user['active']:
            if youngest is None or user['age'] < youngest['age']:
                youngest = user
    return youngest

# Tests
if __name__ == "__main__":
    print("Test 1:", get_active_adults(users))

    print("Test 2:", count_by_role(users))

    print("Test 3:", youngest_active(users))
