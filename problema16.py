sumatoria = 0
contador = 0

for i in range(10):
    valor = float(input(f"Ingrese el valor {i+1}: "))
    
    if 5 <= valor <= 2500:
        sumatoria += valor
        contador += 1

if contador > 0:
    promedio = sumatoria / contador
    print(f"El promedio de los valores comprendidos entre 5 y 2500 es: {promedio}")
else:
    print("No se ingresaron valores válidos en el rango de 5 a 2500.")
