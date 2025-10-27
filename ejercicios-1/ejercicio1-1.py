
#datos

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#diferencia de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(f'el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'el curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')