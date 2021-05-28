# Curso de Python - Nivel Básico 2021

### Proyecto:
* Aplicación Supermercado (Consola)

### Temas:
* Variables y Tipos de Datos
* Numeros y Operadores Aritmeticos
* Operadores y Operaciones
* Condicionales (IF-ELFE-ELIF)
* Bucles (FOR-WHILE)
* Datos con Métodos (Listas-Diccionarios-Strings)
* Funciones (def-lambda)

### Instalación Librerias
1. Primero Instalar pip (https://phoenixnap.com/kb/install-pip-windows#ftoc-heading-4)
2. Instalar Libreria PrettyTable (https://pypi.org/project/prettytable/)
3. Comando: **pip install prettytable**
4. How to use: 

> from prettytable import PrettyTable

> x = PrettyTable()

> x.field_names = ["City name", "Area", "Population"]

> x.add_row(["Adelaide", 1295, 1158259])

> x.add_row(["Brisbane", 5905, 1857594])

> print(x)