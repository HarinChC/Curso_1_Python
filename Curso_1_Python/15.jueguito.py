import random

print("!Bienvenido al juego de adivina un numero¡")
print("Trata de adivinar un numero entre en 1 y el 5")
NumeroR = random.randint(0,2)
NumA =int(input("ingrese el numero de la tabla que requiere  :"))
if NumA == NumeroR:
    print("!FELICITACIONES ADIVINASTE EL NUMERO¡")
else:
    print("no adivinaste el numero intenta nuevamente")