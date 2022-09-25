userWeight = 0
oneKg = 0.45
oneLbs = 2.20

def convertWeight():
    userWeight = int(input("Weight:" ))
    kgOrLbs = input("(K)g or (L)bs ?")
    K=""
    L=""
    if kgOrLbs == K:
        userWeight *= oneLbs
        print(userWeight)
    elif kgOrLbs == L:
        userWeight *= oneKg
        print(userWeight)

convertWeight()

