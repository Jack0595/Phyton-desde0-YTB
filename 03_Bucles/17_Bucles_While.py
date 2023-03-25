i = 1
while i <= 10:
	print("Ejecución " + str(i))
	i = i + 1

print("Termino el bucle")


# genera un bucle hasta que se introdusxa una edad positiva
edad = int(input("Introduce  tu edad por favor: "))

while edad < 0:   # while edad < 5 or edad > 110:
	print("Haz introducido ua edad negativa. Vuelve a intentarlo")
	edad = int(input("Introduce tu edad por favor: "))

print("Gracias por tu colaboracion, puedes pasar")
print("Edad del aspirante" + str(edad))



# crear un programa que regrese la raiz cuadrada de un numero
import math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un número: "))

intentos = 0

while numero < 0:
	print("No se peede hallar la raiz cuadrada de un número negativo")

	if intentos == 2:
		print("Haz consumido demasiados intentos. El programa ha finalizado")
		break;  # forza la salida del bucle while

	numero = int(input("Introduce un número: "))

	if numero < 0:
		intentos = intentos + 1

if intentos < 2:
	solucion = math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) " es " + str(solucion))
