frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = ("hola joaco")
numeros = [2, 5, 8, 10]
#evitando que se coma una granada con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f"me voy a comer una {fruta}")

#evitando que el bucle se siga ejecutando con break
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == 'pera':
        break
    

print("bucle terminado")

#recorrer una cadena de texto

for letra in cadena:
    print(letra)

#for en una sola linea de codigo, duplicamos los numeros
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)