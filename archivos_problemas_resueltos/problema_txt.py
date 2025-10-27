#haz 2 listas, una con nombres y otra con apellidos

nombres = ["lucas", "joaco", "jesus", "mateo", "juan"]
apellidos = ["perez", "svoboda", "jones", "smith", 'messi']

#registrar esta info en un txt de forma optima

with open("archivos_problemas_resueltos/nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n")
    [arch.writelines(f"nombre: {n}\napellido: {a}\n---------------\n") for n,a in zip(nombres,apellidos)]

