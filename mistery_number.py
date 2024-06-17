#Mistery number game in french
import random

mistery_number = random.randint(1, 100)
tentatives_max = 5

print("*** Le jeu du nombre mystère ! ***")
print(f"Il te reste {tentatives_max} essais ")

for essais in range(tentatives_max, 0, -1):
    tentatives = input("Devine le nombre : ")

    if not tentatives.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    tentatives = int(tentatives)
    print(f"Il te reste {essais - 1} essais ")

    if tentatives == mistery_number:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère en {tentatives_max - essais + 1} tentatives.")
        break
    print("Le nombre mystère est plus grand." if tentatives < nombre_mystere else "Le nombre mystère est plus petit.")
else:
    print(f"Dommage ! Le nombre mystère était {mistery_number}")
    print("Fin du jeu.")

#Xafiq
