def frase(nombre,apellido,adjetivo):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('joaco','svoboda','capo')

#creando la misma funcion con un parametro opcional y un valor por defecto

def frase(nombre,apellido,adjetivo = 'tonto'):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('joaco','svoboda')

print(frase_resultante)