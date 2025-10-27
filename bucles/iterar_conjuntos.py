
animales = {"gato", "perro", "loro", "cocodrilo"}

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

numeros = {10, 2, 3, 5}
for numero in numeros:
    resultado = numero * 10
    print(resultado)

for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#rangos con  range

for num in range(3, 18):
    print(num)


#forma correcta de recorrer un conjunto con enumerate

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es {valor}")

#usando el for / else

for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")

#todo esto funciona para listas y tuplas
