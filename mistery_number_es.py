import random

numero_misterioso = random.randint(1, 100)
intentos_max = 5

print("*** ¡El juego del número misterioso! ***")
print(f"Te quedan {intentos_max} intentos.")

for intentos in range(intentos_max, 0, -1):
    adivinanza = input("Adivina el número: ")

    if not adivinanza.isdigit():
        print("Por favor, introduce un número válido.")
        continue

    adivinanza = int(adivinanza)
    print(f"Te quedan {intentos - 1} intentos.")

    if adivinanza == numero_misterioso:
        print(f"¡Felicidades! Encontraste el número misterioso en {intentos_max - intentos + 1} intentos.")
        break
    print("El número misterioso es más grande." if adivinanza < numero_misterioso else "El número misterioso es más pequeño.")
else:
    print(f"¡Qué lástima! El número misterioso era {numero_misterioso}.")
    print("Fin del juego.")

#Xafiq
