#conjuntos (set): coleccion no ordenada de elementos no duplicados

frutas = {"manzana", "naranja", "mandarina", "naranja"}
print(frutas)        # {'manzana', 'naranja', 'mandarina'} (el duplicado se ignora)
print(type(frutas))  # set
print(len(frutas))   # 3

for item in frutas:
    print(item)  # Puede salir en cualquier orden.

conjunto = {"Python", 156, True}
print(conjunto)      # Orden no garantizado.
print(type(conjunto))# 


print("manzana" in frutas)  # True
print("pera" in frutas)     # False

frutas.add("pera")
frutas_tropicales = {"piña", "mango"}
frutas.update(frutas_tropicales)  # también funciona con listas o tuplas
print(frutas)

frutas.remove("mango")   # ok si "mango" está; error si no.
frutas.discard("pera")   # ok esté o no esté "pera".

eliminado = frutas.pop()  # elemento al azar
print(eliminado)
frutas.clear()
print(frutas)             # set()

A = {"A", "B", "C"}
B = {"C", "D", "E"}

C_union = A.union(B)             # {'A', 'B', 'C', 'D', 'E'}
I_inter = A.intersection(B)      # {'C'}
D_diff  = A.difference(B)        # {'A', 'B'}

print(C_union)
print(I_inter)
print(D_diff)

numeros = [1, 2, 2, 3, 3, 3]
unicos = list(set(numeros))
print(unicos)  # [1, 2, 3] (el orden puede variar)