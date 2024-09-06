import random

class Personage:
    def __init__(self, nom):self.nom = nom;self.pv = 50;self.potions = 3 
    def attaquer(self, cible): 
        d = random.randint(5, 10); cible.pv -= d;
        print(f"💥 {self.nom} attaque {cible.nom} et inflige {d} points de dégâts.")

    def boire_potion(self): 

        if self.potions > 0:
            soin = random.randint(15, 50);self.pv += soin; self.potions -= 1
            print(f"🥰 {self.nom} vous buvez une potion et récuperez {soin} points de vie. ")
            print(f"Vous avez {self.pv} points de vie.")
            print(f"{ennemi.nom} a {ennemi.pv} a points de vie.")
        else:
            print(f" 😳 {self.nom} vous n'avez plus de potions. 😳 ")
            print(f"Il reste {self.pv} points de vie.")
            print(f"{ennemi.nom} a {ennemi.pv} a points de vie.")
           
    def est_vivant(self): return self.pv > 0

print("\n-- 🕹️  80's Game 🕹️ --")
self, ennemi = Personage(input("\nNom du Joueur : ")), Personage("Ennemi")
print(f"""\n{self.nom} a {self.pv} points de vie. {"---🎮---"} {ennemi.nom} a {ennemi.pv} points de vie.""")

while self.est_vivant() and ennemi.est_vivant(): 
    a = input(f"\n{'- -'*30}\nSouhaitez-vous attaquer (1) 🗡  ou utiliser une potion (2) 🧪 ? : ")
    if a == "1":
        self.attaquer(ennemi) and ennemi.est_vivant(); 
        ennemi.attaquer(self);print("- - -"*15)
        print(f"{self.nom} il vous reste {self.pv} points de vie."); 
        print(f"Il reste {ennemi.pv} points de vie à votre ennemi.")
    elif a == "2": 
        self.boire_potion();ennemi.attaquer(self)
    else:
        print(f"\n😵 Action non valide, choisissez (1) ou (2). 😳 \n{'- -'*60}")

if self.est_vivant(): print(f"\n 😎 Félicitations {self.nom}, vous avez gagné ! 😎 ")  
else: print(f"\n 😵 Désolé {self.nom}, vous avez perdu. 😵")

#Xafiq
