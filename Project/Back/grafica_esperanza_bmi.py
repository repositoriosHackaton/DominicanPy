import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Project/Back/BD/datos_arreglados2.csv')

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.scatter(df['bmi'], df['life_expectancy'])

# Agregar título y etiquetas
plt.title('Esperanza de vida en muncion del indice de masa corporal')
plt.xlabel('Esperanza de vida')
plt.ylabel('Indice de masa corporal')

# Guardar la gráfica en un archivo
plt.tight_layout()
plt.savefig('expectativa_vida_peso.png', format='png', dpi=300)

# Mostrar la gráfica
plt.show()