for i in range(5):  # devuelve 5 elementos empezando desde [0,1,2,3,4]
	print(f"Valor de la variable: {i}")


for i in range(5,10): # devuelve elementos entre 5 y 10, empezando en 5 y menores a 10 [5,6,7,8,9]
	print(f"Valor de la variable: {i}")


for i in range(5,50,3):  # devuelve elementos entre 5 y 50, dando saltos de 3 
	print(f"Valor de la variable: {i}")


print(len("Juan"))  # len <- regresa la cantidad de caracteres que tiene una cadena



# uso de range y len anidado para evaluar una cadena de texto
valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
	if email[i] == "@":
		valido = True

if valido:
	print("Email correcto")
else: 
	print("Email incorrecto")