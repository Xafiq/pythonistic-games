import random

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pv = 50
        self.pociones = 3

    def atacar(self, objetivo):
        d = random.randint(5, 10)
        objetivo.pv -= d
        print(f"💥 {self.nombre} ataca a {objetivo.nombre} e inflige {d} puntos de daño.")

    def beber_pocion(self):
        if self.pociones > 0:
            curacion = random.randint(15, 50)
            self.pv += curacion
            self.pociones -= 1
            print(f"🥰 {self.nombre} bebe una poción y recupera {curacion} puntos de vida.")
            print(f"Tienes {self.pv} puntos de vida.")
            print(f"{enemigo.nombre} tiene {enemigo.pv} puntos de vida.")
        else:
            print(f"😳 {self.nombre}, ya no te quedan pociones. 😳")
            print(f"Te quedan {self.pv} puntos de vida.")
            print(f"{enemigo.nombre} tiene {enemigo.pv} puntos de vida.")
    
    def esta_vivo(self):
        return self.pv > 0

print("\n-- 🕹️  Juego de los 80 🕹️ --")
jugador, enemigo = Personaje(input("\nNombre del Jugador: ")), Personaje("Enemigo")
print(f"""\n{jugador.nombre} tiene {jugador.pv} puntos de vida. {"---🎮---"} {enemigo.nombre} tiene {enemigo.pv} puntos de vida.""")

while jugador.esta_vivo() and enemigo.esta_vivo():
    accion = input(f"\n{'- -'*30}\n¿Deseas atacar (1) 🗡 o usar una poción (2) 🧪? : ")
    if accion == "1":
        jugador.atacar(enemigo) and enemigo.esta_vivo()
        enemigo.atacar(jugador)
        print("- - -" * 15)
        print(f"{jugador.nombre}, te quedan {jugador.pv} puntos de vida.")
        print(f"Le quedan {enemigo.pv} puntos de vida a tu enemigo.")
    elif accion == "2":
        jugador.beber_pocion()
        enemigo.atacar(jugador)
    else:
        print(f"\n😵 Acción no válida, elige (1) o (2). 😳 \n{'- -'*60}")

if jugador.esta_vivo():
    print(f"\n😎 ¡Felicidades {jugador.nombre}, has ganado! 😎")
else:
    print(f"\n😵 Lo siento {jugador.nombre}, has perdido. 😵")

#Xafiq
