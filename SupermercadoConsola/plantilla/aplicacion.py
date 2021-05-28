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
	print("Agregando producto")

def Eliminar():
	print("Eliminando producto")

def Ver(lista=None,encab=None):
    print("Viendo productos")