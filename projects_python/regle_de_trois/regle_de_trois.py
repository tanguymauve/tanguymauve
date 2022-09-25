a = 0
b = 0 
c = 0
d = 0
def regle_de_trois():
    c = float(input("Le premier nombre à mulitiplier ="))
    b = float(input("Le deuxième nombre à mulitiplier ="))
    a = float(input("Le dénominateur(le nombre correspondant à l'inconnu) ="))
    
    d = (c * b)/a
    d = f"{d:.6f}"
    print(d)


regle_de_trois()