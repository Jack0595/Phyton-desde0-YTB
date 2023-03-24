miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(miDiccionario)

print(miDiccionario["Francia"])

print(miDiccionario["España"])

miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

miDiccionario["Italia"] = "Roma"
print(miDiccionario)

del miDiccionario["Reino Unido"]
print(miDiccionario)


miDiccionario2 = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario2)


miTupla  = ("España", "Fracia", "Reino Unido", "Alemania")
miDiccionario3 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}
print(miDiccionario3)

print(miDiccionario3[miTupla[1]])

print(miDiccionario3["Alemania"])


miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":(1991,1992,1993,1996,1997,1998)}
print(miDiccionario4["Anillos"])


miDiccionario5 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario5)
print(miDiccionario5.keys())
print(miDiccionario5.values())
print(len(miDiccionario5))






