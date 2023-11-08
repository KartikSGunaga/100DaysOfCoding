print("Welcome to PyPassword Generator!")

import random as rd
import string as st

length = int(input("How many characters would you like: "))
chars = int(input("How many symbols: "))
num = int(input("How many numbers: "))

total_chars = length + chars + num

letters = st.ascii_letters
numbers = [number for number in range(11)]
special_characters_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "-", "_", "=", "+", ";", ":", ",", ".", "<", ">", "?", "/", "\\", "|"]

password_list = []

for i in range(length):
    password_list.append(rd.choice(letters))

for i in range(chars):
    password_list.append(rd.choice(special_characters_list))

for i in range(num):
    password_list.append(rd.choice(numbers))

password = ""
rd.shuffle(password_list)

for char in password_list:
    password += str(char)

print(f"Your password is: {password}")


