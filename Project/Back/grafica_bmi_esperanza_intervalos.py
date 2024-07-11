import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Project/Back/BD/datos_arreglados2.csv')
df = df[df['intervals_bmi'] != 'Bajo peso']


# Definir los rangos de edad
bins = [20, 30, 40, 50, 60, 70]
labels = ['20-29', '30-39', '40-49', '50-59', '60-69']

# Crear una nueva columna con los rangos de edad
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

average_bmi = df.groupby('intervals_bmi')['life_expectancy'].mean()

# Crear la gráfica de barras
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(average_bmi.index, average_bmi, color='#1f77b4', edgecolor='black')

# Agregar etiquetas y título
ax.set_title('Promedio de esperanza de vida por Rango de IMC', fontsize=15)
ax.set_xlabel('Rango de IMC', fontsize=12)
ax.set_ylabel('Promedio de esperanza de vida', fontsize=12)

# Agregar etiquetas de datos en las barras
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2), ha='center', fontsize=12)

# Estilizar la gráfica
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.xaxis.set_ticks_position('none')

# Guardar la gráfica en un archivo
plt.tight_layout()
plt.savefig('promedio_bmi_por_edad_intervalos.png', format='png', dpi=300)

# Mostrar la gráfica
plt.show()