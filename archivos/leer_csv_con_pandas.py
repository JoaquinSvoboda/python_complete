import pandas as pd

#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos/datos.csv")
df2 = pd.read_csv("archivos/datos.csv")


#obteniendo los datos de la columna nombre
nombres = df["nombres"]

cadena = "0123456789"


#ordenando por edad el dataframe
df_ordenado = df.sort_values("edad")


#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])


#accediendo a la fila que quiera
primer_fila = df.head(1)

#accediendo a las ultimas filas
ultima_fila = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales = df.shape

#obteniendo data estadistica
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a todas las filas de uan columna
apellidos = df.iloc[:,1]

#accediendo a todas las filas de edad mayor a 30
mayor_que_33 = df.loc[df["edad"]>33,:]

print(mayor_que_33)