#consigna: falto el profe y los alumnos van a armar la clase

#pedir el nombre y la edad del compañero

#funcion para obtener al asistente y el profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
   #creando la lista con los companeros 
    compañeros = []
   #ejecutando un for para pedir la info de cada companero 
    for i in range(cantidad_de_compañeros):
        nombre = input('ingrese el nombre del compañero: ')
        edad = int(input('ingrese la edad del compañero: '))
        compañero = (nombre,edad)
        #agregando la info a la lista
        compañeros.append(compañero)
    #ordenandolos de menos a mayo segun la edad
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor
#companero devuelve una tupla con (nombre, edad) y despues accedemos al nombre
#para definir al asistente y al profesor
asistente,profesor = obtener_compañeros(5)

print(f'el asistente es: {asistente}')
print(f'el profesor es: {profesor}')