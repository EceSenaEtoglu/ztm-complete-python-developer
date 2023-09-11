import re

def is_a_valid_email(email):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if pattern.search(email):
        return True
    else:
        return False


email1 = "alexa@gmail.com"
email2 = "gibberish"

print(is_a_valid_email(email1))  # True
print(is_a_valid_email(email2))  # False


# At least 8 char long
# contain any sort letters,numbers, $%#@
# has to end with a number  (just a dummy rule as an exercise)

def is_a_valid_password(password):

    regex = r"^[a-zA-Z0-9$%#@]{7,}[0-9]$"

    pattern = re.compile(regex)

    if pattern.search(password):
        return True
    else:
        return False


pass1 = "123AFG@8"
pass2 = "_12345678"
pass3 = "ABCD90"

print(is_a_valid_password(pass1))  # True
print(is_a_valid_password(pass2))  # False
print(is_a_valid_password(pass3))   # False
