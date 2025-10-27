with open("archivos/texto.txt",'w', encoding="UTF-8") as archivo:
    for i in range(5):
        archivo.write(f"linea {i+1} agregada \n")