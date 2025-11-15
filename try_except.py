try:
    print("Intentamos algo")
except:
    print("Captura error")


# Sin manejo:
resultado = 10 / 0  # Provoca ZeroDivisionError

# Con manejo específico:
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero.")


# Sin manejo:
print(x)  # Provoca NameError

# Con manejo específico:
try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida.")

# Con error presente:
try:
    print(x)  # x no definida
except NameError:
    print("Esta variable no ha sido definida.")
finally:
    print("Esto se ejecuta siempre.")

# Sin error:
x = 1
try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida.")
finally:
    print("Esto se ejecuta siempre.")


