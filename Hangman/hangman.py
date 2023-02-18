#Variables
word_to_guess = "france"
length_of_word = len(word_to_guess)
discovered_letters =[]
screen = []


#Functions
    #Back End
#Permet de check le match entre l' inpunt user et une lettre dans le mot à deviner
#Permet ensuite de prendre l'index de la lettre deviné dans la liste mot_a_deviner, l'enlève et la met dans discovered_letter
def guess_the_word():
    global screen
    screen = []
    screen = ['_'] * length_of_word
    if word_to_guess.__contains__(user_letter_guess):
        for i, letter in enumerate(list_word_to_guess):
            if letter == user_letter_guess:
                discovered_letters.append(user_letter_guess)
                list_word_to_guess[i] = None

        for i, letter in enumerate(word_to_guess):
            if letter in discovered_letters:
                screen[i] = letter
        print(''.join(screen)+"\n")
    else:
        print("MIIIIIPPP wrong\n")

#Permet de transformer la string mot mystère en une liste. Liste nécessaire pour enlever au fur et à mesure les lettres déja devinés
def string_converter(string):
    global list_word_to_guess
    list_word_to_guess = []
    list_word_to_guess[:0] = string
    return list_word_to_guess
    
    
#Front End
    #Permet d'afficher les barres du jeu et de les remplacer par les lettres 
def screen_display():
    global screen
    screen = []
    screen = ['_'] * length_of_word
    screen[0] = user_letter_guess
    print(screen)
    #mettre la lettre de la liste word_to_guess
    #dans la liste de screen display dans le même index
    

#Process
string_converter(word_to_guess)
print(f'The word have ' + str(length_of_word) + ' letters')
user_letter_guess = input("Guess a letter: ")
while True:
    #set(discovered_letters) != set(word_to_guess)
    guess_the_word()
    print( "Discovered letters so far: ",discovered_letters, "\n")
    user_letter_guess = input("Guess another letter: ")
    
    if set(discovered_letters) == set(word_to_guess):
        print(f'Congrats ! The word was {word_to_guess}!')
        break

#to-do : add the hangman and the "guessing the entire word" function