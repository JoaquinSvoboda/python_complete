#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"impresionante, cometiste el siguiente error: {err}")
#lanzando mi propia excepcion
raise MiExcepcion("jjaajajajaj persona poco instruida")
#manejandola
try:
    raise MiExcepcion("jjaajajajaj persona poco instruida")
except:
    print("como vas a cometer ese error?")