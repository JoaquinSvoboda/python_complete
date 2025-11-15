"""
¿Cómo abrir y leer archivos con open y with?
Leer un archivo requiere indicar su nombre y el modo. 
Con open("archivo.txt", "r") se intenta abrir en lectura. 
Si el archivo no existe, aparece un error específico: FileNotFoundError.

Usa readline() para leer la primera línea.
Cierra el archivo si lo abriste manualmente.
Para automatizar el cierre, utiliza el contexto with.
¿Qué hace open con el modo r?
Ejemplo básico de lectura de una línea con manejo de error mediante try/except:"""

try:
    f = open("archivo.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo")

"""
¿Por qué conviene usar with para archivos?
El contexto with abre y cierra por ti, lo que evita fugas y ahorra código."""

try:
    with open("archivo.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")

"""
Tip práctico: si al ejecutar ves el mensaje de “No se ha encontrado el archivo” aun teniendo el archivo creado, revisa la carpeta desde la que corres el proyecto. Debes estar dentro de la carpeta correcta usando el comando de terminal: cd manejo de archivos.

¿Cómo solucionar problemas de acentos con encoding UTF-8?
Si ves caracteres raros en tildes o eñes, especifica la codificación UTF-8 al abrir:
"""

with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.readline())

"""
¿Qué diferencias hay entre los modos r, w, a y x?
Cada modo define cómo se manipula el archivo. Elegir bien el modo evita pérdidas de datos o errores inesperados.

Modo "r" (read): lectura. Da error si el archivo no existe.
Modo "w" (write): escritura. Sobrescribe si existe; si no existe, lo crea.
Modo "a" (append): agrega al final. No borra lo anterior.
Modo "x": crea un archivo nuevo. Da error si ya existe.
¿Cómo escribir y luego leer con w?
Al escribir con w, el contenido previo se pierde. Luego puedes leer lo recién escrito.

"""

# Escribir (sobrescribe)
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("hola mundo desde write en el with\n")

# Leer lo escrito
with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.readline())

"""
¿Cómo agregar sin borrar con append?
Usa a para sumar contenido. Añade un salto de línea con "\n" si quieres separar entradas.
"""
with open("archivo.txt", "a", encoding="utf-8") as f:
    f.write("\n")
    f.write("hola mundo desde write en el with")

with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.read())  # Lee todo el archivo

"""
¿Cómo manejar errores y crear archivos si no existen?
Puedes “atrapar” el error de lectura, crear el archivo y continuar el flujo normal. Así integras lectura, creación y escritura en una sola secuencia controlada.
"""
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
    # Crear el archivo vacío si no existe
    open("archivo.txt", "x").close()
    # Escribir y leer a continuación
    with open("archivo.txt", "w", encoding="utf-8") as f:
        f.write("hola mundo desde write en el with\n")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())

"""
Claves que pondrás en práctica: 
- Función integrada open: nombre del archivo y modo. 
- Modos: r, w, a, x y sus efectos. 
- Lecturas: readline() para una línea, read() para todo. 
- Escritura: write() y salto de línea con "\n". 
- Contexto with: abre y cierra automáticamente. 
- Errores: FileNotFoundError con try/except. 
- Codificación: UTF-8 para acentos y eñes. 
- Ruta de ejecución: asegúrate de estar en la carpeta correcta con cd.
"""