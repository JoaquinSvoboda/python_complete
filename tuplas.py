# TUPLAS: coleccion ordenada e inmutable de elementos que permiten duplicados

tecnologias = ("Python", "JavaScript", "Go", "python")
print(type(tecnologias))           
print(tecnologias[1])
print(len(tecnologias))

fruta = ("manzana")
print(type(fruta))                 

fruta = ("manzana",)
print(type(fruta))                 

tupla = ("Python", 5, True)
print(tupla)                   
print(type(tupla))   
tupla = ("Python", 5, True)
x, y, z = tupla
print(x)           
print(y)   
print(z)        

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2
print(tupla3)                    

print(tupla * 2) 

for item in tupla:
    print(item)

tupla_a_modificar = ("Python", "JavaScript", "Go")

lista_comodin = list(tupla_a_modificar)   # casting a lista
lista_comodin.append("React JS")          # modificar con append
tupla_a_modificar = tuple(lista_comodin)  # volver a tupla

print(tupla_a_modificar)                  # ('Python', 'JavaScript', 'Go', 'React JS')