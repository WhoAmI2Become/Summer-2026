# ============================================
# Password Strength Checker
# Concepts: functions, loops, conditionals
# ============================================

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"

# --- Main ---
password = input("Enter your password: ")
result = check_strength(password)
print(f"Password strength: {result}")