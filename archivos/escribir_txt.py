with open("archivos/texto.txt",'w', encoding="UTF-8") as archivo:
    #sobreescribimos el archivo
    #archivo.write("jajajaj te la re contra teclee")
    archivo.writelines(["Hola maestro como andas?", "misericordia"])

    #si en lugar de usar w usamos a (append) en vezz de sobreescribir, agrega info