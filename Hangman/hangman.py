#Variables
word_to_guess = "capybara"
length_of_word = len(word_to_guess)
discoverd_letters =[]
screen = []


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

def screen_display():
    global screen
    screen = len(list_word_to_guess)*"_ "
    #mettre la lettre de la liste word_to_guess (warning il faut qu'elle soit convert)
    #dans la liste de screen display dans le même index
    screen[:0]=screen
    local_index = 0
    screen[local_index] = user_letter_guess
    print(''.join(screen))

#Process
string_converter(word_to_guess)
print(f'The word have ' + str(length_of_word) + ' letters')
while len(list_word_to_guess) > 0:
    
    user_letter_guess = input("Guess a letter\n")
    screen_display()
    guess_the_word()
    print("Discover letter so far : ", discoverd_letters)
    user_letter_guess = input("Guess another letter\n")
    
print(f'Congrats ! The word was {word_to_guess}!')