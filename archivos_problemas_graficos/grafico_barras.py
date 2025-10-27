import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_graficos/joaco_ingresos.csv')

#creando un grafico
sns.barplot(x='fuente',y='ingresos',data=df)

#mostrar el total de ingresos
total_ingresos = df['ingresos'].sum()
#mostrar el total
print(f'el total de ingresos es: ${total_ingresos}usd')
#mostrando el grafico
plt.show()