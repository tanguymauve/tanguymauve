#Variables
word_to_guess = "france"
length_of_word = len(word_to_guess)
discoverd_letters =[]
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
        index = list_word_to_guess.index(user_letter_guess)
        screen[index] = user_letter_guess
        print(screen)
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
user_letter_guess = input("Guess a letter\n")
while len(list_word_to_guess) > 0:
    
    guess_the_word()
    #screen_display()
    print("Discover letter so far : ", discoverd_letters)
    user_letter_guess = input("Guess another letter\n")
    
print(f'Congrats ! The word was {word_to_guess}!')