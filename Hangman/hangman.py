#Variables
word_to_guess = "capybara"
length_of_word = len(word_to_guess)
user_letter_guess = input("Guess a letter\n")
discoverd_letters =[]


#Functions
    #Back End
#Permet de vérifier si l'input user contient une lettre du mot mystère, et retire la lettre correspondante
def guess_the_word():
    if word_to_guess.__contains__(user_letter_guess):
        index = list_word_to_guess.index(user_letter_guess)
        list_word_to_guess.pop(index)
        discoverd_letters.append(user_letter_guess)
        print(f"There is indeed a {user_letter_guess} in the secret word")
    else:
        print("MIIIIIPPP wrong")

#Permet de transformer la string mot mystère en une liste. Liste nécessaire pour enlever au fur et à mesure les lettres déja devinés
def string_converter(string):
    global list_word_to_guess
    list_word_to_guess = []
    list_word_to_guess[:0] = string
    return list_word_to_guess
    #Front End

def screen():
    for i in range(length_of_word):
        print(''.join("_"))

#Process
while list_word_to_guess:
    string_converter(word_to_guess)
    guess_the_word()
    print(''.join(list_word_to_guess))
    print(''.join(discoverd_letters))