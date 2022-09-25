userWeight = 0
oneKg = 0.45
oneLbs = 2.20

def convertWeight():
    userWeight = int(input("Weight:" ))
    kgOrLbs = input("(K)g or (L)bs ?")
    if kgOrLbs == "K":
        userWeight *= oneLbs
        print("Your weight in Lbs is", userWeight, "Lbs")
    elif kgOrLbs == "L":
        userWeight *= oneKg
        print("Your weight in Kg is", userWeight, "Kg")

convertWeight()

