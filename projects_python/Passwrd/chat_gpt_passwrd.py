import random as rd

numbers = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyz'
passwrd = []
i = 0
length = input('How many characters do you want in your password?\n')

while i < int(length):
    passwrd.append(rd.choice(numbers))
    passwrd.append(rd.choice(letters)) 
    i += 1

print(''.join(passwrd))
