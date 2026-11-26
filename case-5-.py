password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
has_space = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch.isspace():
        has_space = True
    else:
        has_special = True

errors = []

if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")

if not has_upper:
    errors.append("Add at least one uppercase letter.")

if not has_lower:
    errors.append("Add at least one lowercase letter.")

if not has_digit:
    errors.append("Add at least one digit.")

if not has_special:
    errors.append("Add at least one special character.")

if has_space:
    errors.append("Spaces are not allowed.")

if len(errors) == 0:
    print("Valid password")
else:
    print("Invalid password. Correct these conditions:")
    for error in errors:
        print("-", error)