#Variables
mot_a_deviner = "etre"
longueur_du_mot = len(mot_a_deviner)
lettres_decouvertes =[]
progression_ecran = ['_'] * longueur_du_mot
mot_a_deviner_format_liste =[]
lettre_de_user = ''

#Convertie une string en liste
def string_converter(string):
    global list_word_to_guess
    list_word_to_guess = []
    list_word_to_guess[:0] = string
    return list_word_to_guess

#Vérifie la présente de la lettre user dans le mot à deviner
def is_the_letter_in_the_word():
    if mot_a_deviner.__contains__(lettre_de_user):
        for i, letter in enumerate(mot_a_deviner_format_liste):
            if letter == lettre_de_user:
                lettres_decouvertes.append(lettre_de_user)
                mot_a_deviner_format_liste[i] = None
            else :
                print("Wrong")

#Affiche l'écran
     
def affichage_ecran():
    for i, letter in enumerate(mot_a_deviner):
            if letter in lettres_decouvertes:
                screen[i] = letter
    print(''.join(screen)+"\n")
        

#Code
string_converter(mot_a_deviner)
lettre_de_user = input("Guess a letter: ")
while True:
    is_the_letter_in_the_word()
    print( "Discovered letters so far: ",lettres_decouvertes, "\n")
    user_letter_guess = input("Guess another letter: ")