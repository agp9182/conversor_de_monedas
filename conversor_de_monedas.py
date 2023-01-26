import os
os.system("cls")

def conversor (moneda):
    dolares = int(input("¿Cuantos dolares tienes?: "))
    pesos = dolares * moneda
    print(f"Tienes {pesos} pesos")

USD = 1
ARS = 290 
COP = 4600
MXN = 20

print("Bienvenido al conversor de monedas")
print("Elige una de las siguienes opciones de conversion")
print("1 - Dolares a Pesos Argentinos")
print("2 - Dolares a Pesos Colombianos")
print("3 - Dolares a Pesos Mexicanos")
opcion = input("¿Cual es tu opcion?: ")
opcion = int(opcion)

if opcion == 1: 
    pesos_argentinos = conversor(ARS)
elif opcion == 2:
    pesos_colombianos = conversor(COP)
elif opcion == 3:
    pesos_mexicanos = conversor(MXN)
else:
    print("Escribe una opcion correcta!")