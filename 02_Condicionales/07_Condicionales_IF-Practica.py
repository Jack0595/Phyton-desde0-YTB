print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad, por favor: "))

if edad_usuario < 18:		# IF puede usarse sin su else
	print("No puedes pasar")
elif edad_usuario > 100:
	print("Edad incorrecta")
else:						# else siempre tiene que venir acompañado de un IF
	print("Puedes pasar")

print("El programa ha finalizado")



print("Verificacion de notas")

nota_alumno = int(input("Introduce una nota: "))

if nota_alumno < 5:
	print("Insuficiente")

elif nota_alumno < 6:
	print("Suficiente")

elif nota_alumno < 7:
	print("Bien")

elif nota_alumno < 9:
	print("Notable")

else:
	print("Sobresaliente")
