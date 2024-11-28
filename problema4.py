#Calcular la nota del trimestre a partir de tres notas, luego determinar si aprobó o
#debe recuperar e informarlo.

nota1 = int(input("ingrese nota 1"))
nota2 = int(input("ingresenota 2"))
nota3 = int(input("ingrese nota3"))
promedio = (nota1+nota2+nota3)/ 3
if promedio >= 70:
    print ("aprobo")
elif promedio <70:
    print("no aprobo")
