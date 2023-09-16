#PROMEDIO DE NOTAS ESTUDIANTES

Total = 5 + 4 + 3
Promedio1 = Total/3
print("el promedio de las notas es ",Promedio1)

nota1 =int(input("¿cual es su PRIMERA nota? "))
nota2 =int(input("¿cual es su SEGUNDA nota? "))
nota3 =int(input("¿cual es su TERCERA nota? "))

def promedio2(nota1, nota2, nota3):
    Total = nota1 + nota2 + nota3
    Promedio = Total/3
    print("su promedio es :",Promedio)
    return Promedio

print("//////////")
variable = promedio2(nota1,nota2,nota3)
print("la variable es ",variable)