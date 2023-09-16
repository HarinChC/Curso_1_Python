import random

print("!Bienvenido al juego de adivina un numero¡")
print("Trata de adivinar un numero entre en 1 y el 5")
NumeroR = random.randint(0,3)
adivinado = False
while not adivinado:
      NumA =int(input("ingrese el numero :"))
      if(NumA == NumeroR):
        print("!FELICITACIONES ADIVINASTE EL NUMERO¡")
        adivinado=True 
#print("el numero era :",NumeroR)
      
          
   
