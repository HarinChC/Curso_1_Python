def saludo():
    print("hola amigo")
saludo()


def saludo2(nombre):
    print(f"hola amigo {nombre}")
saludo2("HARIN")

def saludo3(nombre,apellido):
    print(f"hola amigo {nombre}")
    print(f"tu apellido es  {apellido}")
saludo3("carlos","chaverra")

def multiplicacion(num1,num2):
    print("la multiplicacion de",num1, "*", num2,"es igual a ")
    total =num1*num2
    print(total)

multiplicacion(9,10)