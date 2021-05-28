# Programa Interaccion Consola
from aplicacion import Agregar,Ver,Eliminar

# Variables del programa
menu = """========== MENU ==========
1) Agregar producto
2) Eliminar producto
3) Ver productos
4) Salir"""

# Ciclo principal de interaccion
while True:
	print(menu)
	opc = int(input(">> "))

	if opc==1:
		Agregar()
	elif opc==2:
		Eliminar()
	elif opc ==3:
		Ver(lista_productos)
	elif opc==4:
		print("Adios, gracias por tu visita!!!")
		break
	else:
		print("opcion incorrecta elija otra")
