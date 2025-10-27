
numeros = [1,2,3,4,5,6,7,8,9]

#creo una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2

#creando funcion comun que diga si es par o impar
#def es_par(num):
#    if(num%2==0):
 #       return True

#usando filter con una funcion comun
#numero_pares = filter(es_par, numeros)

#hago lo mismo pero con lambda
numero_pares = filter(lambda numeros:numeros%2==0, numeros)

print(list(numero_pares))