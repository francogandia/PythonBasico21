# Archivo Principal de la Aplicacion
from aplicacion import Agregar,Ver,Eliminar

# Supermercado
lista_productos = [	["pan",3],
					["gaseosa",2]	]

horario = {	"Lunes":[10,18],
			"Martes":[14,18],
			"Miercoles":[10,18]	}
for key in horario:
	print(f"Los {key} hace horarios de {horario[key][0]} a {horario[key][1]}")

menu = """========== MENU ==========
1) Agregar producto
2) Eliminar producto
3) Ver productos
4) Salir"""

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
		print("Adios")
		break
	else:
		print("opcion incorrecta elija otra")
