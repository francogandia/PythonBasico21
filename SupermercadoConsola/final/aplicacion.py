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
				"nombre":"Tomates",
				"cantidad":500,
				"precio_u":199.0		},

			{	"id":4,
				"nombre":"Facturas",
				"cantidad":180,
				"precio_u":229.0		},

			{	"id":5,
				"nombre":"Fideos",
				"cantidad":600,
				"precio_u":82.0			}	
											]

encabezados_carrito = ["producto","id","nombre","cantidad","precio_u","precio_c"]

carrito = []

def Agregar():
	print("Seleccione un producto de la lista para AGREGARLO:")
	Ver(stock,encabezados_stock)
	eleccion = input("Numero del producto>> ") # "1"
	ID = int(eleccion) # "1" -> 1
	cantidad = float(input("Que cantidad quiere comprar? >> "))

	numProducto = len(carrito)
	productoAgregar = {	"producto":numProducto+1, # cuantos productos tengo + 1
						"id":ID, #
						"nombre":stock[ID-1]["nombre"], # lo tengo que buscar en stock por fila
						"cantidad":cantidad,
						"precio_u":stock[ID-1]["precio_u"], # lo tengo que buscar en stock
						"preico_c":stock[ID-1]["precio_u"]*cantidad	}

	agregando = PrettyTable()
	agregando.field_names = encabezados_carrito
	agregando.add_row(productoAgregar.values())

	carrito.append(productoAgregar)
	print("Se agrego:\n",agregando)

def Eliminar():
	print("Seleccione un producto de la lista para ELIMINARLO:")
	Ver(carrito,encabezados_carrito)
	eleccion = input("Numero del producto>> ") # "1"
	numProducto = int(eleccion) # "1" -> 1

	productoEliminar = carrito.pop(numProducto-1) # se elimina

	# numProducto = 2
	# numProducto-1 = 1
	pos = numProducto-1
	prod = numProducto

	for producto in carrito[pos:len(carrito)]:
		producto["producto"] = prod
		prod+=1

	eliminando = PrettyTable()
	eliminando.field_names = encabezados_carrito
	eliminando.add_row(productoEliminar.values())
	print("Se elimino:\n",eliminando)

def Ver(lista=None,encab=None):
	if lista == None: # por defecto tome la tabla del stock
		listaProductos = carrito
		encabezados = encabezados_carrito
	else: # sino que tome la tabla que se le pase
		listaProductos = lista
		encabezados = encab

	if len(listaProductos)>0:
		tabla = PrettyTable() # creo la tabla
		tabla.field_names = encabezados # creo los encabezados

		for producto in listaProductos:
			#print(producto)
			tabla.add_row(producto.values()) # agrego cada producto

		print(tabla) # muestro la tabla
	else:
		print("No hay productos para mostrar")