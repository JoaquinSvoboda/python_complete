
"""¿Qué es una función en Python y cómo se define?
Una función es un bloque de código que solo se ejecuta cuando la llamamos. 
Se define con def y un nombre, seguido de dos puntos, e incluye instrucciones indentadas que se correrán al invocarla.
 Al llamarla, abrimos y cerramos paréntesis para ejecutar la acción. Llamarla varias veces repite su efecto, 
lo que fomenta la reutilización y la modularización."""


# definir
def mi_funcion():
    print("Hola mundo desde una función")

# invocar (se ejecuta cada vez que se llama)
mi_funcion()
mi_funcion()

"""¿Cómo personalizar con argumentos y parámetros?
Para personalizar, se añaden argumentos en la definición. Por ejemplo, un nombre que se usa dentro de la función. Si no se usa, suele verse “apagado” en el editor, indicando que debería aprovecharse o eliminarse.

Argumentos: variables que la función “espera” en su definición.
Parámetros: valores que “le pasamos” al llamarla.
En la práctica, muchas veces se usan indistintamente."""

# un argumento
def saludar(nombre):
    print("Hola,", nombre)

saludar("Pedro")
saludar("María")

"""Si se esperan varios argumentos, el orden importa. Faltará 
un argumento obligatorio si no lo pasas, y Python mostrará un error."""

# varios argumentos y orden estricto
def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")

saludar("Pedro", "Sánchez")
saludar("María", "Gutiérrez")

"""¿Cómo usar valores por defecto para evitar errores?
Puedes asignar valores por defecto y así no fallará si omites alguno al llamar.
Un caso útil es un string vacío para apellido o una nacionalidad por defecto.
"""

# valores por defecto
def saludar(nombre, apellido="", nacionalidad="Colombia"):
    # ejemplo de personalización con valores por defecto
    if apellido:
        print(f"Hola, {nombre} {apellido} de {nacionalidad}")
    else:
        print(f"Hola, {nombre} de {nacionalidad}")

saludar("Pedro", "Sánchez", "España")      # Hola, Pedro Sánchez de España
saludar("María", "Gutiérrez")               # Hola, María Gutiérrez de Colombia
saludar("Ana")                               # Hola, Ana de Colombia

""" Las funciones pueden devolver información con return. 
Si no asignas el resultado, no verás nada en pantalla. 
Asigna a una variable y luego imprime."""

def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
print(resultado)  # 5

def funcion():
    pass  # evita error mientras decides la lógica