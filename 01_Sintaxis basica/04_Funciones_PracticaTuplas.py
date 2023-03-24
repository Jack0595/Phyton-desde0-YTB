miTupla = ("Juan", 13,1,1995,13)
print(miTupla[:])

print(miTupla[1])

print(miTupla[3])

print("Juan" in miTupla)

print(miTupla.count(13))

print(len(miTupla))

miLista = list(miTupla)
print(miLista[:])

miLista.append("Sarai")

miTupla2 = tuple(miLista)
print(miTupla2[:])

tuplaUnitaria = ("Armando",)
print(len(tuplaUnitaria))

miTupla3 = "Luis", 15,8,1264  # no se recomienda porque puede confundirnos
print(miTupla3[:])

nombre, dia, mes, agno = miTupla3  #desempaquetado de tupla
print(nombre)
print(dia)
print(mes)
print(agno)

