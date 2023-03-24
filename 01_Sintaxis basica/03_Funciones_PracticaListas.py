miLista=["Maria", "Pepe", "Marta", "Antonio"]

print(miLista[:]) # imprime toda la cadena

print(miLista[2])  # imprime el elemento 2 de la lista 

print(miLista[-3]) # imprime Pepe, empiza contand desde -1 del final al principio

print(miLista[0:2])  

print(miLista[0:1])

print(miLista[1:2])

print(miLista[2:]) 

miLista.append("Sandra")
print(miLista[:])

miLista.insert(2,"Carlos")
print(miLista[:])

miLista.extend(["Ana","Lucia","Tere"])
print(miLista[:])

print(miLista.index("Antonio"))

print("Pepe" in miLista)  # devuelve boolean al comprobar si el elemento se encuentra dentro de la lista
print("Pepess" in miLista)


miLista2=["Maria", 5, True, 78.35]
miLista2.extend(["Sandra", "Ana", "Lucia"])
print(miLista2[:])

miLista2.remove("Ana")
print(miLista2[:])

miLista2.pop()
print(miLista2[:])


miLista3 = miLista + miLista2
print(miLista3[:])

print(miLista2*2)

