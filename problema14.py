#Ingresar 10 valores numéricos por teclado y calcular la suma, el promedio e
#imprimir la suma, el promedio agregando una leyenda en cada caso.
suumatoria=0

for numero in range(10):
    valor=float(input("Ingrese un valor"))
    sumatoria+=valor
promedio=sumatoria/10
print(f"La sumatoria es :{sumatoria}")
print(f"El promedio es :{promedio}")
