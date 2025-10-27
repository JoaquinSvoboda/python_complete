archivo_sin_leer = open("archivos/texto.txt", encoding="UTF-8")
#archivo = archivo_sin_leer.read()
#linea = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()

#cerramos el archivo
archivo_sin_leer.close()

print(linea)