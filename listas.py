# LISTAS: son ordenadas, modificables y permiten ser duplicadas

frutas = ["manzana", "naranjas", "mandarinas", "naranja"]
print(frutas)
print(type(frutas))
frutas[1]="bananas"
print(frutas[1])

lista = ["joaco", 2, True]
print(lista)
print(type(lista))
print(len(lista))

print(frutas[0:3])
print(frutas[0:])

if "manzana" in frutas:
    print("la manzana es parte de las frutas")


vehiculos = ["autos", "motos", "aviones"]

#APLICAMOS METODOS
#METODO APPEND: agrega un elemento al final de la lista

vehiculos.append("barcos")
print(vehiculos)

#METODO INSERT: indico en que posicion de la lista agrego un nuevo elemento

vehiculos.insert(1, "bicicletas")
print(vehiculos)

#METODO REMOVE:
vehiculos.remove("autos")
print(vehiculos)

#METODO POP: remueve un elemento indicando el indice
vehiculos.pop(1)
print(vehiculos)

#METODO SORT: ordena alfabeticamente la lista
vehiculos.sort()
print(vehiculos)

#METODO REVERSE: ordena al reves alfabeticamente
vehiculos.reverse()
print(vehiculos)

#METODO EXTEND: modifica permanentemente la lista agregando otra lista
colec1 = [1,2,3]
colec2 = [4,5,6]
colec1.extend(colec2)
print(colec1)


