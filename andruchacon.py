
print("Funcion de resta de dos numeros")

def resta_num (n1, n2):
    return n1 - n2

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
resta = resta_num(num1, num2)

print("La resta entre ", num1," y ", num2," es: ",resta)
