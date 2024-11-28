#Dados 3 números determinar el mayor e informar por pantalla el resultado
num1=float(input("Digite un primer numero:"))
num2=float(input("Digite un segundo numero:"))
num3=float(input("Digite un  tercer numero:"))

if num1>= num2 and num1>= num3:
    mayor=num1
elif num2>=num1 and num2>=num3:
    mayor= num2
else:
    mayor= num3
print("El mayor numero es:",mayor)
