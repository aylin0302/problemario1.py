# Ingresar 10 valores por teclado y obtener la sumatoria de los mismos. Imprimir los
#resultados.
suma= 0
for num in range(10):
    suma+=float(input("ingresa un valor"))
    print("La suma de los valores es:", suma)
