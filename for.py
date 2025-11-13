palabra = "python"

for letra in palabra:
    print(letra)

frutas = ["manzana", "naranja", "kiwi"]

for fruta in frutas:
    if fruta == "naranja":
        break
    print(fruta)
else:
    print("ya hemos terminando el bucle for")

print("-----------------------------------")

# range
#comienza en el numero cero y termina en el numero que asignamos sin incluirlo
for i in range(10):
    print(i)

print("-----------------------------------")


for i in range(3,5):
    print(i)

print("-----------------------------------")

#va del cero al 10 de 2 en 2

for i in range(0,11,2):
    print(i)

print("-----------------------------------")


adjetivos = ["rica", "saludable"]
frutas = ["manzana","naranja","kiwi"]


for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)

print("-----------------------------------")

for i in range(3,5):
    pass


