multiples = """
Hola 
mundo
desde
tucuman
argentina
"""

print(multiples)

palabra = "murcielago"
print(len(palabra))

texto = "este curso es de fundamentos de python"
esta_incluida = 'python' in texto
print(esta_incluida)

no_esta_incluido = 'javascript' not in texto
print(no_esta_incluido)

mayuscula = texto.upper()
print(mayuscula)
minuscula = texto.lower()
print(minuscula)

espacios = "    Esto es un texto     "
sin_espacios = espacios.strip()
print(sin_espacios)

#indice 01234
texto = "Este es un texto"
# slicin es seleccionar una partes especifica del texto
print(texto[7:16])
print(texto[:-2])

#modificar texto con REPLACE
curso = " este curso es de javascript"
print(curso.replace("javascript", "python"))

#separar texto con split
texto_dividido = texto.split( )

print(texto_dividido)

#Normailzacion

texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print("mayusculas".lower() in texto2.lower())