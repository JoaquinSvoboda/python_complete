#conjuntos con SET

conjunto = set(["dato1","dato2"])

print(type(conjunto))

#metiendo un conjunto dentro de otro conjunto
#frozenset es para meter un conjunto dentro de otro conjunto

conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1, 'dato3'}

print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#verificamos si es un subconjunto
resultado = conjunto1.issubset(conjunto2)

#verificamos si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)

#verificar si hay algun numero en comun( cuando un elemento coincide, da false)
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
