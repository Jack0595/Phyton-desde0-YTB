# Crea un programa que pida dos números por teclado. 
# El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

def DevuelveMax(num1, num2):
	if num1 > num2:
		print(f"El numero ´{num1} es mayor")
	elif num2 > num1:
		print(f"El numero ´{num2} es mayor")
	else: 
		print("Son iguales")



nume1 = int(input("Ingresa el primer numero: "))

nume2 = int(input("Ingresa el segundo numero: "))

DevuelveMax(nume1, nume2)