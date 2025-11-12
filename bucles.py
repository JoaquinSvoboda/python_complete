# 1 a 9
i = 1
while i < 10:
    print(i)
    i += 1

# Imprime 1 a 5 y se detiene
i = 1
while i <= 10:
    if i == 5:
        break
    i += 1
    print(i)

# Imprime 1, 2, 3, 4, 6, 7, 8, 9, 10 (saltea el 5)
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print('i dejó de ser menor a diez')