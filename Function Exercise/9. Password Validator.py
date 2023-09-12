def valid_pass(password):
    digits = 0
    passlen = True
    alphanum = True
    two_digits = False
    if not(6 <= len(password) <= 10):
        passlen = False
        print("Password must be between 6 and 10 characters")
    if not(password.isalnum()):
        alphanum = False
        print("Password must consist only of letters and digits")
    for char in password:
        if char in "1234567890":
            digits += 1
            if digits >= 2:
                two_digits = True
                break
    if not two_digits:
        print("Password must have at least 2 digits")
    if two_digits and alphanum and passlen:
        print("Password is valid")


pword = input()
valid_pass(pword)
