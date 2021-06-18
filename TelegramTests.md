# Encuestas de Telegram Sobre Python 3


## Variables
- - - 
1. ¿Cuál es una asignación correcta de una variables?
* 1ernombre = "Lucas"
* **miApellido = "Trubiano"**
* mi-edad = 23
* estoy aprendiendo = "Python"
> 1 ) No pueden empezar con números. Pero si los pueden contener.
>
> 2 ) No pueden tener símbolos, ni espacios. Excepto el __
>
> 3 ) Admiten letras mayúsculas y minúsculas.

- - - 
2. ¿Qué variable está mal declarada?
* miNombre = "Lucas"
* mi_apellido = "Trubiano"**
* _edad = 23
* **My-name = "Python"**
> Las variables si pueden empezar con __
> 
> Pero no pueden contener. Símbolos como - @ $ ! ~ + , ;

- - - 
3. ¿Es igual una variables ***nombre*** que ***Nombre***?
* Si, son iguales.
* **No, son distintas.**
> Las variables en Python son ***case sensitive***. Sensibles a mayúsculas y minúsculas osea que son variables distintas, igual que si se llamaran distinto.

## Tipos de Datos
- - -
3. **miEdad = "23"** ¿Qué tipo de dato es?
* Un número entero (int).
* Un número decimal (float).
* **Una cadena de texto (str).**
* Un booleano (bool).
> El tipo de dato es **str** porque está definido entre **comillas** " "
- - -
4. Si creo una variable **pesos = 1100** y luego ejecuto **pesos = 1299.9** ¿Qué pasa con el valor de la variable?
* El valor queda 1299
* El valor queda 1299.9
* El programa da SyntaxError
* El programa da TypeError
> El tipo de dato puede cambiar por lo tanto el nuevo valor es 1299.9, no se redondea ni da error.