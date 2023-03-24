# Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el 
# mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

nombre = input("Intoduce el Nombre: ")

apellido = input("Introduce el Apellido: ")

telefono = input("Introduce el telefono: ")

lista_datos = [nombre, apellido, telefono]

print (f"Los datos personales son: Nombre - {lista_datos[0]}, Apellido - {lista_datos[1]}, telefono - {lista_datos[2]}")
