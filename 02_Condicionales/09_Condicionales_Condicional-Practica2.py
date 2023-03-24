print("Programa de becas Año 2023")

distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el n° de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anuel bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
	print("Tienes derecho a la beca")

else:
	print("No tienes derecho a beca")


if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
	print("Tienes derecho a la beca")

else:
	print("No tienes derecho a beca")