import random

nombre_mystere = random.randint(1, 100)
tentatives_max = 5

print("*** Le jeu du nombre mystère ! ***")
print(f"Il te reste {tentatives_max} essais.")

for essais in range(tentatives_max, 0, -1):
    tentative = input("Devine le nombre : ")

    if not tentative.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    tentative = int(tentative)
    print(f"Il te reste {essais - 1} essais.")

    if tentative == nombre_mystere:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère en {tentatives_max - essais + 1} tentatives.")
        break
    print("Le nombre mystère est plus grand." if tentative < nombre_mystere else "Le nombre mystère est plus petit.")
else:
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}.")
    print("Fin du jeu.")

#Xafiq
