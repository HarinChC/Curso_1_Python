import random

print("!Bienvenido al juego de adivina un numero¡")
print("Trata de adivinar un numero entre en 1 y el 10")
NumeroR = random.randint(0,10)
adivinado = False
while not adivinado:
      NumA =int(input("ingrese el numero :"))
      if(NumA == NumeroR):
        print("!FELICITACIONES ADIVINASTE EL NUMERO¡")
        adivinado=True 
      elif NumA>NumeroR:
          print("El numero ingresado es mayor al que vamos a adivinar")
      elif NumA<NumeroR:
          print("El numero ingresado es menor al que vamos a adivinar")
          
#print("el numero era :",NumeroR)
      
          
   
