import random

list = ["casserole","jardin","barcelone","evacuation"]
word = random.choice(list)

tentatives = 7
affichage = ""
lettres_trouvees = ""


for i in word:
    affichage = affichage + "_ "

print(" A vous de jouer !! ")

while tentatives > 0:
    print("Mot à deviner : ", affichage)
    proposition = input("proposez une lettre :")

    if proposition in word:
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bien joué !")
    else:
        tentatives -= 1
        print("-> Dommage, il te reste",tentatives," tentatives")


    affichage = ""
    for x in word:
        if x in lettres_trouvees:
            affichage += x + " "
            print("la")
        else:
            affichage += "_ "

if "_" not in affichage:
    print(">>> Gagné! <<<")
    

print(" fin de la partie")