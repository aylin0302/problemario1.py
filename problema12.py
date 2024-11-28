#Ingresar valores por teclado y acumularlos en una variable detener el proceso
#cuando la suma supere los 78500, al final imprimir el resultado

resultado=0

while resultado<=78500:
    valor=float(input("Ingrese un valor:"))
    resultado+=valor
    
print(f"El resultado es :{resultado}")
