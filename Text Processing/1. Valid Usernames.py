passwords = input().split(", ")
valid = []
for password in passwords:
    if 3 <= len(password) <= 16 and " " not in password and (password.isalnum() or "-" in password or "_" in password):
        valid.append(password)

for pswrd in valid:
    print(pswrd)