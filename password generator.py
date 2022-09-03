from random import randint
from string import punctuation

# All uppercase
password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lowercase
password_1 = ""
for i in range(5):
    i = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password_1 = str(password_1) + i + j
print(password_1)

# special chars
special_chars = list(punctuation) # 32 elements

password_2 = ""
for i in range(5):
    # uppercase letter
    a = chr(randint(65, 90))
    # lowercase letter
    b = chr(randint(65,90)).lower()
    # special character
    c = special_chars[randint(0, 31)]
    password_2 = password_2 + a + b + c
print(password_2)