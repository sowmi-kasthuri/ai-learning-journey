# Password checker
''' ----------------------- RULES --------------------------
Minimum length: 8
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character from a short set, e.g. !@#$%^&*()-_+=
----------------------------------------------------------------'''

while True:
    pwd = input("Enter a password or type exit : ").strip()

    if pwd.lower() in ('exit','quit'):
        break

    if not pwd:
        print("Password cannot be empty")
        continue

    length = len(pwd)
    uppercase = any(c.isupper() for c in pwd)
    lowercase = any(c.islower() for c in pwd)
    digit = any(c.isdigit() for c in pwd)
    special_chars = "!@#$..."
    special = any(c in special_chars for c in pwd)

    fail = []
    
    if length < 8:
        fail.append("Too Short")
    if length > 16:
        fail.append("Too Long")
    if not uppercase:
        fail.append("Missing Uppercase")
    if not lowercase:
        fail.append("Missing Lowercase")
    if not digit:
        fail.append("Missing Digits")
    if not special:
        fail.append("Missing Special Chars") 

    if not fail:
        print("✅ Strong Password")
    else:
        print(" ---------- Weak Password -------- \n")
        for  f in fail:
            print(f"❌ - {f} \n")
