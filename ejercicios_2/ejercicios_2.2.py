#creando una funcion que nos devuelva los numeros primos
#entre el 0 y el argumento que pasamos
#crear una funcion que vea si un numero es primo
def es_primo(num):
    for i in range(2,num-1):
        #si es divisible por alguno retomamos false
        if num%i==0: return False
    #si tenmina el bucle significa que no fue divisible 
    return True

#creando una func que retorne una lista con todos los num primos
def primo_hasta(num):
    #creamos la lista
    primos =[]
    for i in range(2, num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso que lo sea agregamos a la lista
        if resultado == True: primos.append(i)

    #devolvemos la lista
    return primos

resultado = primo_hasta(1000)
print(resultado)