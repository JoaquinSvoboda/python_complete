def crear_contrasenia_random(num):
    chars = "absjfkfef"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contrasenia)

crear_contrasenia_random(9)