print("Programa de evaluacion de notas de alumnos")

# Para ingresar datos uso el enter, no sirve con el intro de la calculadora
# Para poder utilizar input necesitaos abrir la consola, en Tools -> SublimeREPL -> Python -> Run current file

nota_alumno = int(input("Introduce la nota del alumno: "))
# la funcion input simpre devuleve un String, por tanto al ingresar numeros debemos usar int()
# int() tranforma cadenas o caracteres a enteros, solo si son numeros

def evalucaion(nota):
	valoracion = "aprobado"
	if nota<5:
		valoracion = "suspenso"
	return valoracion


print(evalucaion(nota_alumno))

print(evalucaion(4))

print(evalucaion(8))

