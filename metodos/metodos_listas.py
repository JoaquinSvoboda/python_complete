
#creando una lista con list

lista = list(["hola","joaco",36])


#len devuelve la cantidad de elementos de una lista

lista = list(["hola","joaco",36])

resultado = len(lista)

#append agrega elementos de una lista

lista = list(["hola","joaco",36])

resultado = lista.append("jajajaja")

#insert agrega elementos de una lista en un indice especifico

lista = list(["hola","joaco",36])

resultado = lista.insert(2, "jajajaja")

#extend agrega varios elementos de una lista 

lista = list(["hola","joaco",36])

resultado = lista.extend([2, "jajajaja", False])

#pop eliminando elementos de una lista por su indice

lista.pop(0)

#remove eliminando elementos de una lista por su valor

lista.remove("joaco")

#clear eliminando todos los elementos de una lista

#lista.clear()

#sort ordena todos los elementos de una lista de manera ascendente(solo numeros)

lista2 = list([0, 3, 15, 24, 14, 32])

lista2.sort()

#sort con reverse = true los ordena a la inversa

lista2 = list([0, 3, 15, 24, 14, 32])

lista2.sort(reverse = True)

#reverse ordena todos los elementos de una lista de manera descendente( para todos los valores, no solo numeros)

lista2 = list([0, 3, 15, 24, 14, 32])

lista2.reverse()

print(lista2)