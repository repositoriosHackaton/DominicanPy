import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Project/Back/BD/datos_arreglados2.csv')



# Definir los rangos de edad
bins = [20, 30, 40, 50, 60, 70]
labels = ['20-29', '30-39', '40-49', '50-59', '60-69']

# Crear una nueva columna con los rangos de edad
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

average_life_expectancy = df.groupby(['age_group', 'smoker'])['life_expectancy'].mean().unstack()

# Crear la gráfica de barras agrupadas
fig, ax = plt.subplots(figsize=(12, 6))
average_life_expectancy.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e'], edgecolor='black')

# Agregar etiquetas y título
ax.set_title('Expectativa de Vida Promedio por Rango de Edad: Fumadores vs No Fumadores', fontsize=15)
ax.set_xlabel('Rango de Edad', fontsize=12)
ax.set_ylabel('Expectativa de Vida Promedio', fontsize=12)
ax.legend(['No Fumadores', 'Fumadores'], title='Smokers')

# Agregar etiquetas de datos en las barras
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.1f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10)

# Estilizar la gráfica
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
ax.xaxis.set_ticks_position('none')

# Guardar la gráfica en un archivo
plt.tight_layout()
plt.savefig('expectativa_vida_fumadores.png', format='png', dpi=300)

# Mostrar la gráfica
plt.show()