import re

#la cadena en la que se buscan los patrones
text = "la fecha es 23/06/2025 y el telefono es +1-555-555-5555"

#el patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

#el texto con el que se reemplazara el patron
replacement = "fecha oculta"

#reemplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)

#mostramos resultado
print("texto modificado", new_text)