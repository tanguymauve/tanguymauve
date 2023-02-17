#Variables
word_to_guess = "capybara"
length_of_word = len(word_to_guess)
discoverd_letters = []
screen = []


#Functions
#Back End
#Permet de vérifier si l'input user contient une lettre du mot mystère, et retire la lettre correspondante
def guess_the_word():
    if user_letter_guess in word_to_guess:
        index = word_to_guess.index(user_letter_guess)
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
def screen_display():
    global screen
    screen = list(screen)
    for i, letter in enumerate(word_to_guess):
        if letter in discoverd_letters:
            screen[i*2] = letter
        else:
            screen[i*2] = "_"
    screen = "".join(screen)
    print(screen)


#Process
string_converter(word_to_guess)
print(f'The word has {length_of_word} letters')
screen = "_" * (length_of_word * 2 - 1)
print(screen)
while len(word_to_guess) > 0:
    user_letter_guess = input("Guess a letter\n")
    guess_the_word()
    screen_display()
    if user_letter_guess not in word_to_guess:
        word_to_guess = word_to_guess
    else:
        word_to_guess = word_to_guess.replace(user_letter_guess, "")
    if len(word_to_guess) == 0:
        break

print(f'Congrats! The word was {word_to_guess}!')
