# imprime un hola por cada elemento de la lista
for i in ["Pildoras", "Informatica", 3]:
	print("Hola")


for i in ["Pildoras", "Informatica", 3]:
	print("Hola", end="")


for i in ["Pildoras", "Informatica", 3]:
	print("Hola", end=" ")

# impirme un hola por cada caracter
for i in "juan@pildorasinformaticas.es":
	print("Hola", end=" ")

print("")



# corrección de la funcion de de evaluar email
email4 = False
existearroba = False
miEmail = input("Introduce tu dirección de correo: ")

for i in miEmail:
	if(i == "@"):
		existearroba = True
	if(existearroba and i == "."):
		email4 = True

if email4:
	print("Email es correcto 4")
else:
	print("El email no es correcto 4")



# verifica si el tetxo es un correo (al detectar el @)
email = False

for i in "juan@pildorasinformaticas.es":
	if (i =="@"):
		email = True

if email == True:  # para verfificar si es verdadero podemos solo escribir * if email
	print("Email es correcto")
else:
	print("El email no es correcto")



email2 = False
miemail = input("Introduce tu dirección de email: ")

for i in miemail:
	if (i == "@"):
		email2 = True

if email:
	print("Email es correcto")
else:
	print("El email no es correcto")



# en lugar de ealuar asignar contador
contador = 0
email3 = input("Introduce tu dirección de correo: ")

for i in email3:
	if (i == "@" or i == "."):
		contador += 1

if contador == 2:
	print("Email es correcto")
else:
	print("Email no es correcto")






# uso de Range() rango
for i in range(5):
	print("Hola")


