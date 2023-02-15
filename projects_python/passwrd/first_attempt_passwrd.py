import random as rd

numbers = [0,1,2,3,4,5,6,7,8,9]
letters = ['a', 'b', 'c', 'd', 'e']
i = 0
length = input("How long is your password ?\n")
#passwrd = []

'''
while i < int(length):
    passwrd.append(rd.choice(numbers))
    passwrd.append(rd.choice(letters))
    i += 1
'''

while i < int(length):
    print(rd.choice(numbers)).strip
    print(rd.choice(letters)).strip
    i += 1

#print(passwrd)


