# ============================================
# Day 4 Project: Multi-User Login System
# Concepts: dictionaries, loops, if/else
# ============================================

# --- User Database ---
users = {
    "zeke2rich": "Password!1",
    "Rich4Eva": "WeakPass",
    "JOHNDOE": "PASSMESum"
}

# --- Get Username ---
username = input("Enter your username: ")

# --- Login System ---
if username in users:
    correct_password = users[username]
    attempts_left = 3

    while attempts_left > 0:
        password = input("Enter your password: ")

        if password == correct_password:
            print(f"Access granted! Welcome, {username}!")
            break
        else:
            attempts_left -= 1
            print(f"Wrong password. {attempts_left} attempts left.")

    if attempts_left == 0:
        print("Account locked. Too many failed attempts.")

else:
    print("User not found.")