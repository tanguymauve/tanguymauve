from tkinter import *

fenetre = Tk()

for ligne in range(3):
    label = Label(fenetre, text="Texte par défaut").grid(row=1, column=2)
    
    for colonne in range(3):
        value = StringVar() 
        value.set("")
        entree = Entry(fenetre, textvariable="string", width=10).grid(row=1, column=2)
        Button(fenetre, text='1', borderwidth=1).grid(row=4, column=1)
        Button(fenetre, text='2', borderwidth=1).grid(row=4, column=2)
        Button(fenetre, text='3', borderwidth=1).grid(row=4, column=3)
        Button(fenetre, text='4', borderwidth=1).grid(row=3, column=1)
        Button(fenetre, text='5', borderwidth=1).grid(row=3, column=2)
        Button(fenetre, text='6', borderwidth=1).grid(row=3, column=3)
        Button(fenetre, text='7', borderwidth=1).grid(row=2, column=1)
        Button(fenetre, text='8', borderwidth=1).grid(row=2, column=2)
        Button(fenetre, text='9', borderwidth=1).grid(row=2, column=3)
        Button(fenetre, text='0', borderwidth=1).grid(row=5, column=2)

def recupere():
    showinfo("Alerte", entree.get())

value = StringVar() 
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)

bouton = Button(fenetre, text="Valider", command=recupere)
fenetre.mainloop()