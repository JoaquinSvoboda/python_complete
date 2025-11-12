x = 5
y=3
z=5


# Comparaciones con or
# Verdadero si al menos una condición se cumple.
print((x == y) or (y == z))
print(x != y)

# Ejemplo con mayor que para mantener el mismo flujo de comprobación
print((x == y) or (y > z))

# Ambas condiciones son falsas → resultado False
resultado = (x == y) or (y > z)
print(resultado)  # False si ninguna se cumple

# Negación con not
estado = True
print(not estado)  # False

estado = False
print(not estado)  # True

# Negar una comparación
print(not (x == y))  # True si x no es igual a y

print(x >= y)
print(x <= y)

print(x > y and y > z) #FALSE porque las 2 condiciones deben ser true
print(x > y or y > z) #TRUE solo una debe ser true



print(not(True))
print(not(False))

