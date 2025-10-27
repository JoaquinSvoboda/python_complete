import re

texto = """hola maestro esta es la linea 1. cadena como estas? 
Esta es la linea 2 de texto.
y esta es la linea 3 final definitiva mi estimado"""
#haciendo una busqueda simple
resultado = re.findall("esta",texto,flags=re.IGNORECASE)

#\d busca digitos numericos del 0 al 9
resultado = re.findall(r"\d",texto)

#\D busca todo menos digitos numericos del 0 al 9
resultado = re.findall(r"\D",texto)

#\w busca todo caracter alfanumerico
resultado = re.findall(r"\w",texto)

#\w busca todo caracter que no sea alfanumerico
resultado = re.findall(r"\W",texto)

#\s busca espacios en blanco
resultado = re.findall(r"\s",texto)

#armando una cadena de busqueda
resultado = re.findall(r"\d\.\s",texto)


#\ cancela caracteres especiales
resultado = re.findall(r"\.",texto)

#\ cancela caracteres especiales
resultado = re.findall(r"\.",texto)

print(resultado)