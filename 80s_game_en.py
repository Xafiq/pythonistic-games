import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.potions = 3

    def attack(self, target):
        damage = random.randint(5, 10)
        target.hp -= damage
        print(f"💥 {self.name} attacks {target.name} and inflicts {damage} points of damage.")

    def drink_potion(self):
        if self.potions > 0:
            heal = random.randint(15, 50)
            self.hp += heal
            self.potions -= 1
            print(f"🥰 {self.name} drinks a potion and recovers {heal} health points.")
            print(f"You have {self.hp} health points.")
            print(f"{enemy.name} has {enemy.hp} health points.")
        else:
            print(f"😳 {self.name}, you have no potions left. 😳")
            print(f"You have {self.hp} health points left.")
            print(f"{enemy.name} has {enemy.hp} health points.")

    def is_alive(self):
        return self.hp > 0

print("\n-- 🕹️  80's Game 🕹️ --")
player, enemy = Character(input("\nPlayer's Name: ")), Character("Enemy")
print(f"""\n{player.name} has {player.hp} health points. {"---🎮---"} {enemy.name} has {enemy.hp} health points.""")

while player.is_alive() and enemy.is_alive():
    action = input(f"\n{'- -'*30}\nDo you want to attack (1) 🗡 or use a potion (2) 🧪? : ")
    if action == "1":
        player.attack(enemy) and enemy.is_alive()
        enemy.attack(player)
        print("- - -" * 15)
        print(f"{player.name}, you have {player.hp} health points left.")
        print(f"The enemy has {enemy.hp} health points left.")
    elif action == "2":
        player.drink_potion()
        enemy.attack(player)
    else:
        print(f"\n😵 Invalid action, please choose (1) or (2). 😳 \n{'- -'*60}")

if player.is_alive():
    print(f"\n😎 Congratulations {player.name}, you won! 😎")
else:
    print(f"\n😵 Sorry {player.name}, you lost. 😵")

#Xafiq
