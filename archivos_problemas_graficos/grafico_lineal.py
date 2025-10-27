import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_graficos/gases.csv')

#creando un grafico
sns.lineplot(x='fecha',y='gases',data=df)
#creando un punto en el momento de mas gases
plt.plot('01-09',17,'o')
#mostrando el grafico
plt.show()