#Ingresar un valor por teclado y determinar si es positivo, negativo o igual a cero,
#imprimir una leyenda en cada caso

valor = float(input("Ingrese un valor: "))

if valor > 0:
    print("El valor es positivo.")
elif valor < 0:
    print("El valor es negativo.")
else:
    print("El valor es cero.")
