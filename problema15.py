# Ingresar 100 valores por teclado y determinar cuántas veces el valor ingresado
#es: a) Mayor a 0 y menor a 10
#b) Esta comprendido entre 10 y 100 ambos inclusive.
#c) Es mayor a 100
#d) Es negativo
#e) Es igual a 0Imprimir los resultados.

MayorOMenor10=0
Entre10Y100=0
Mayor100=0
Negativos=0
Igual0=0

for i in range (100):
    valor= float(input("Ingrese un numero"))
    
    if valor>0 and valor>10:
        MayorOMenor10+=1
    elif 10 <= valor<100:
        Entre10Y100+=1
    elif valor<0:
        negativos+=1
    elif valor==0:
        Igual0+=1
        
print(f"Mayor a 0 y Menor a 10:{MayorOMenor10}")
print(f"Entre 10 y 100:{Entre10Y100}")
print(f"Mayor a 100:{Mayor100}")
print(f"Negativos:{Negativos}")
print(f"Igual a 0:{Igual0}")
