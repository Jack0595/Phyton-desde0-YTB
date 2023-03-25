# ejemplo1 Uso Continue
for letra in "Python":
	if letra == "h":
		continue

	print("Viendo la letra: " + letra)


# ejemplo2  Programa que cuenta los caracteres excepto los espacios
nombre = "Pildoras Informaticas"

contador = 0

for i in nombre:
	
	if i == " ":
		continue
	contador += 1

print(contador)


# Ejemplo3 Uso de Pass

while True:
	pass

class MiClase:
	pass # para implementar mas tarde


# Ejemplo 4 Uso de Else
email = input("Introduce tu email: ")

for i in email:

	if i == "@":
		arroba = True
		break;  # necesario colocar punto y coma
else:
	arroba = False

print(arroba)