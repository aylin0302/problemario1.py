# Ingresar un valor por teclado y determinar si es menor que 10 si está comprendido
#entre 10 y 100 o si es mayor a 100, imprimir una leyenda, repetir el proceso 10 veces.

for valor in range (10):
    nume= float(input("Ingrese un numero"))
    if nume <10:
        print("El nimero es menor que 10")
    elif 10<=nume<=100:
        print("El numero se encuentra entre 10 y 100")
    else:
        print("El numero es mayor que 100")
