
#Un diccionario agrupa información en pares clave: valor separados por comas. La última coma es opcional. Es ideal para dar características a un elemento.

auto = {
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2025
}
print(auto)

#Accede a un valor por su clave con corchetes o con get.

print(auto['marca'])      # Renault
print(auto.get('marca'))  # Renault

#Si quieres solo las claves o solo los valores:
print(auto.keys())    # dict_keys(['marca', 'modelo', 'año'])
print(auto.values())  # dict_values(['Renault', 'Clio', 2025])

#Modificar un valor es como acceder, pero asignando un nuevo dato. También puedes agregar una nueva pareja. 

# Modificar un valor existente
auto['año'] = 2020

# Agregar un nuevo par clave-valor
auto['color'] = 'verde'
print(auto)

#Con update puedes modificar y agregar en una sola línea:
auto.update({'año': 2022, 'puertas': 4})
print(auto)


#Compruebo si una clave existe con in. es case sensitive.
if 'marca' in auto:
    print('Marca es una de las propiedades de este diccionario')

if 'MARCA' in auto:  # no entra por sensibilidad a mayúsculas
    print('No se imprime')

# Eliminar por clave
auto.pop('puertas')

# Eliminar el último par insertado
auto.popitem()

# Vaciar el diccionario por completo
auto.clear()
print(auto)  # {}

# Solo claves
for k in auto:
    print(k)

# Solo valores
for v in auto.values():
    print(v)

# Clave y valor al mismo tiempo
for clave, valor in auto.items():
    print(clave, valor)


#Un diccionario puede contener otros diccionarios como valores: así modelas estructuras con múltiples propiedades por elemento.
familia = {
    'hijo uno':  {'nombre': 'Pedro',   'edad': 8},
    'hijo dos':  {'nombre': 'Ana',     'edad': 7},
    'hijo tres': {'nombre': 'Marcelo', 'edad': 6}
}

print(familia['hijo uno']['nombre'])  # Pedro