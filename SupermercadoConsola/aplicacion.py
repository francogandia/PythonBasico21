# =========================================================
# ================= Capa de Aplicacion ====================
# =========================================================
from prettytable import PrettyTable

encabezados_stock = ["id","nombre","cantidad","precio_u"]

stock = [ 	
			{	"id":1,
				"nombre":"Coca-Cola",
				"cantidad":300,
				"precio_u":174.0		},

			{	"id":2,
				"nombre":"Fernet",
				"cantidad":200,
				"precio_u":607.0		},

			{	"id":3,
				"nombre":"Ron-Malibu",
				"cantidad":150,
				"precio_u":899.0		},

			{	"id":4,
				"nombre":"Andes-Roja",
				"cantidad":600,
				"precio_u":133.0		},

			{	"id":5,
				"nombre":"Malbec",
				"cantidad":200,
				"precio_u":800.0		}	
											]

encabezados_carrito = ["producto","id","nombre","cantidad","precio_u","precio_c"]

carrito = []

def Agregar():
	# Mostrar el catalogo
	print("Elegir un producto de la lista para AGREGAR:")
	Ver(stock,encabezados_stock)
	ID = int(input("Ingrese numero de producto>> ")) # "2" -> 2
	cantidad = float(input("Que cantidad quiere llevar? >> "))
	
	productoAgregar = {	
						"producto":len(carrito)+1, # automatico
						"id":ID,
						"nombre":stock[ID-1]["nombre"],
						"cantidad":cantidad,
						"precio_u":stock[ID-1]["precio_u"],
						"precio_c":cantidad*stock[ID-1]["precio_u"]
																	}

	carrito.append(productoAgregar)

def Eliminar():
	print("Elegir un producto de la lista para ELIMINAR:")
	Ver(carrito,encabezados_carrito)
	prod = int(input("Numero de producto>> ")) # fila 2

	productoEliminar = carrito.pop(prod-1) # devuelve la fila eliminada (subindice 1)

	numProducto = productoEliminar["producto"] # num prod: 2
	for producto in carrito[prod-1:len(carrito)]:
		producto["producto"] = numProducto
		numProducto+=1



def Ver(listaProductos=carrito,encabezados=encabezados_carrito):
	if len(listaProductos)>0:
		#mostrar
		tabla = PrettyTable()
		tabla.field_names = encabezados
		for producto in listaProductos:
			tabla.add_row(producto.values())
		print(tabla)
	else:
		print("No hay productos para mostrar")