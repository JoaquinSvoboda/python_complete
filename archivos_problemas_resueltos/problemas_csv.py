#cambiar el tipo de dato de una columna

import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos/datos.csv")

#convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df["edad"][0]))

#reemplazando los datos "svoboda" por "capo"
df['apellido'].replace('svoboda','capo',inplace=True)

print(df)

#eliminando filas con datos vacios
df = df.dropna()

#eliminar filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe resultante limpio
df.to_csv('archivos_problemas_resueltos/datos_limpios.csv')
