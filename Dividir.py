def fdivision():
  a = int(input("Ingresa el dividendo: "))
  b = int(input("Ingrese el divisor: "))
  if b == 0:
    return "Dividir por CERO?"
  return a / b

print("Tu resultado es", fdivision())