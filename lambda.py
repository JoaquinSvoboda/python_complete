"""
Las lambdas en Python simplifican operaciones puntuales con código claro y directo. Aquí entenderás qué es una función anónima, cómo manejar argumentos y cómo crear una fábrica de funciones para construir un duplicador y un triplicador con poca sintaxis y alto impacto.

¿Qué es una lambda y por qué importa?
Una lambda es una función pequeña y anónima: no tiene nombre, puede recibir varios argumentos, pero contiene una sola expresión. Es ideal para operaciones cortas donde definir una función completa sería más largo.

Sintaxis compacta y legible.
Una sola expresión que se evalúa y retorna.
Útil para cálculos inmediatos.
¿Cuál es la sintaxis de lambda en Python?
Sintaxis básica: palabra clave, argumentos, dos puntos y expresión."""

x = lambda a: a + 10
print(x(5))  # 15

"""
x guarda la lambda.
a recibe 5 y evalúa 5 + 10.
Se imprime 15.
¿Qué recomienda el editor sobre lambda?
En Visual Studio Code aparece una advertencia sugiriendo usar una función común para casos simples. Para fines didácticos, la lambda es suficiente aquí.

¿Cómo usar varios argumentos con lambda?
También puedes pasar múltiples argumentos y operar con ellos en una sola expresión. El caso mostrado: sumar dos números.

¿Cómo sumar argumentos con lambda?"""

x = lambda a, b: a + b
print(x(2, 3))  # 5

"""
a y b reciben 2 y 3.
La expresión suma ambos argumentos.
Devuelve 5 directamente.
¿Por qué se parece a una función común?
El patrón es idéntico a una función de suma tradicional, pero con sintaxis compacta. Sigue siendo una función válida que retorna el resultado de la expresión.

¿Cómo construir una fábrica de funciones con lambda?
El punto fuerte mostrado: usar lambdas para fabricar funciones que aplican una operación parametrizada. Aquí, multiplicar por un número n para crear un duplicador o triplicador.

¿Qué hace mi_función y qué devuelve?"""

def mi_función(n):
    return lambda a: a * n
"""
Recibe n como parámetro de configuración.
Devuelve una lambda que multiplica a por n.
Permite crear funciones especializadas.
¿Cómo crear duplicador y triplicador?"""

duplicador = mi_función(2)
triplicador = mi_función(3)

"""
duplicador multiplica por 2.
triplicador multiplica por 3.
Ambas son funciones lambda resultantes."""

