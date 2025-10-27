#creando una funcion simple
def saludar():
    print("hola joaco, mi amigo, como andas?")

saludar()

#crear una funcion que tenga parametros

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "crack"
    
    print(f"hola {nombre}, mi {adjetivo}, como estas?")

saludar("Joaco", "hoMbre") 
saludar("euge", "mujer") 
saludar("fran", "no-binarie")

#crear una funcion que nos retorne valores
def crear_contrasenia_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasenia

password = crear_contrasenia_random(4)
frase = f"tu contrasenia nueva es: {password}"
print(frase)