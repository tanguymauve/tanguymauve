import random as rd

numbers = [0,1,2,3,4,5,6,7,8,9]
letters = ['a', 'b', 'c', 'd', 'e']
i = 0
length = input("How long is your password ?\n")



while i < int(length):
    print(rd.choice(numbers))
    print(rd.choice(letters))
    i += 1

#print(passwrd)

