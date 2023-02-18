import random

# Words to guess
categories = [
    # Car brands
    ['audi', 'bmw', 'citroen', 'ferrari', 'fiat', 'ford', 'honda', 'lamborghini', 'mercedes', 'renault'],
    # Countries
    ['france', 'italie', 'espagne', 'chine', 'japon', 'portugal', 'canada', 'mexique', 'argentine', 'bresil'],
    # Vegetables
    ['tomate', 'concombre', 'carotte', 'poivron', 'brocoli', 'aubergine', 'oignon', 'ail', 'courgette', 'radis'],
    # Colors
    ['bleu', 'rouge', 'vert', 'jaune', 'orange', 'rose', 'violet', 'marron', 'gris', 'blanc'],
    # Professions
    ['docteur', 'avocat', 'policier', 'acteur', 'peintre', 'architecte', 'veterinaire', 'informaticien', 'boulanger', 'professeur']
]

# Ask the user to choose a category
print("Choisissez une catégorie en tapant le numéro associé à la catégorie :")
print("1: Marques de voitures, 2: Pays, 3: Légumes, 4: Couleurs, 5: Professions")
category_num = int(input())

# Check if the chosen category number is valid
while category_num < 1 or category_num > 5:
    print("Numéro de catégorie invalide. Veuillez choisir un numéro de catégorie entre 1 et 5.")
    category_num = int(input())

# Select the word to guess from the chosen category
word_to_guess = random.choice(categories[category_num-1])

# Initialize the list of used letters
used_letters = []

# Game loop
print(f"Il y a {len(word_to_guess)} lettres dans le mot à deviner.\n")
while True:
    # Display the word to guess with underscores for hidden letters
    hidden_word = ""
    for letter in word_to_guess:
        if letter in used_letters:
            hidden_word += letter
        else:
            hidden_word += "_"
        hidden_word += " "
    print(f"Lettres utilisées : {' '.join(used_letters)}")
    print(hidden_word)

    # Check if the user has won
    if "_" not in hidden_word:
        print(f"Félicitations, vous avez gagné ! Le mot à deviner était {word_to_guess}")
        break

    # Ask the user to guess a letter
    guess = input("Entrez une lettre: ").lower()

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Veuillez entrer une seule lettre.")
        continue
    if guess in used_letters:
        print("Vous avez déjà utilisé cette lettre.")
        continue

    # Add the guess to the list of used letters
    used_letters.append(guess)

    # Check if the guess is correct
    if guess in word_to_guess:
        print(f"La lettre '{guess}' est présente dans le mot à deviner.")
    else:
        print(f"La lettre '{guess}' n'est pas présente dans le mot à deviner.")
