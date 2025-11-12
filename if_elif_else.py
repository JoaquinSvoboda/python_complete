x = 5
y = 3
z = 1

if x > y and x > z:
    print("x es mayor a y y x es mayor a z")
elif y == y:
    print("x es igual a y")
else:
    print("ninguna condicion se cump[lio")

x = 5
y = 3
z = 10

if x > y or x > z:
    print("x es mayor a y y x es mayor a z")
elif y == y:
    print("x es igual a y")
else:
    print("ninguna condicion se cump[lio")


a = "python"
b = "java"
c = "python"

if a == c:
    if a == b:
        print("a es igual a c pero es distinto de b")
    else:
        print("es un else del if interno o anidado")
else:
    print("ninguna condicion se cumplio")

e = 10 
f = 10

if e == f:
    pass        #se usa para omitir el if hasta definir el comportamiento


