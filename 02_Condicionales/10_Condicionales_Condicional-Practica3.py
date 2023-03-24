print("Asignaturas Optativas Año 2023")

print("Asugnaturas optativas: Informatica gráfica - Pruebas de software - Utilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("informatica gráfica", "pruebas de software", "Utilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no está contemplada")