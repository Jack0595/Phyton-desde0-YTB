# Aplicacion por el metodo tradicional
def generaPares(limite):

	num = 1
	miLista = []

	while num < limite:
		miLista.append(num*2)
		num = num + 1

	return miLista

print(generaPares(10))


# Aplicacion por metodo de Generadores

def generaPares2(limite):
	num = 1

	while num < limite:
		yield num*2

		num = num + 1

devuelvePares = generaPares2(10)

# impresion con bucle
#for i in devuelvePares:
#	print(i)

print(next(devuelvePares))
print("Aqui podria ir mas codigo")

print(next(devuelvePares))
print("Aqui podria ir mas codigo")

print(next(devuelvePares))