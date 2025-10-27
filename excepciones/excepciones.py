
#creando una funcion que pide numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input('numero 1: ')
        b = input('numero 2: ')
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanza una excepcion pedir que reingrese los datos
        except Exception as e:
            print('te pedi un numero, no te hagas el gracioso')
            print(f'ERROR: {type(e).__name__}')
        #si todo salio bien terminamos el bucle
        else:
            break
        #pase lo que pase se ejecuta esto
        finally:
            print('esto se ejecuta siempre')
    return resultado
#mostrando el resultado
print(sumar_dos())