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
	print("Agregando producto")

def Eliminar():
	print("Eliminando producto")

def Ver(lista=None,encab=None):
    print("Viendo productos")