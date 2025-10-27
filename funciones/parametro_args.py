
#forma no optima de sumar
def suma(a,b):
    return a + b

resultado = suma(5,3)

#utilizando el parametro agrs
def suma(nombre,*numero):
    return f"{nombre}, la suma de tus numeros es: {sum(numero)}"

resultado = suma("lucas", 5, 3,9,10,20,3)
print(resultado)