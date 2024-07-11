import pandas as pd

df = pd.read_csv('./Project/Back/BD/datos.csv')

df.drop(columns=['no_of_dependents','city','job_title','claim'], inplace=True)
df.dropna(inplace=True)

df['life_expectancy'] = 80

df['sex'] = df['sex'].map({'male': 1, 'female': 0})

bins = [0,18.5,24.9,29.9,34.9,39.9,float('inf')]
labels =['Bajo peso','Adecuado','Sobrepeso','Obsidad grado 1','Obsidad grado 2','Obsidad grado 3']

df['intervals_bmi'] = pd.cut(df['bmi'], bins=bins, labels=labels, include_lowest=True)

#division de los dataframe por sexo
df_female = df[df['sex'] == 0]
df_male = df[df['sex'] == 1]

#calculo de la esperanza de vida de las mujeres
df_female['life_expectancy'] -= df_female['sex'] * 6
df_female['life_expectancy'] -= df_female['smoker'] * 7
df_female['life_expectancy'] += df_female['regular_ex'] * 6
df_female['life_expectancy'] -= df_female['age']
df_female['life_expectancy'] -= df_female['diabetes'] *12
df_female['life_expectancy'] -= (df_female['hereditary_diseases'] == 'Epilepsy') * 6
df_female['life_expectancy'] -= (df_female['hereditary_diseases'] == 'Arthritis') * 4
df_female['life_expectancy'] -= (df_female['hereditary_diseases'] == 'HeartDisease') * 6
df_female['life_expectancy'] -= (df_female['hereditary_diseases'] == 'Cancer') * 12
df_female['life_expectancy'] -= (df_female['hereditary_diseases'] == 'High BP') * 6

df_female['life_expectancy'] -= (df_female['intervals_bmi'] == 'Sobrepeso') * 3
df_female['life_expectancy'] -= (df_female['intervals_bmi'] == 'Obsidad grado 1') * 5
df_female['life_expectancy'] -= (df_female['intervals_bmi'] == 'Obsidad grado 2') * 7
df_female['life_expectancy'] -= (df_female['intervals_bmi'] == 'Obsidad grado 3') * 9


def adjust_life_expectancy(value):
    if value <= 0:
        return 1
    else:
        return value
    
df_female['life_expectancy'] -= (df_female['bmi'] - 40) * 0.75


# Aplicar la función a la columna 'life_expectancy'
df_female['life_expectancy'] = df_female['life_expectancy'].apply(lambda x: adjust_life_expectancy(x))

df_female['life_expectancy'] = df_female['life_expectancy'].round(2)


#calculo de la esperanza de vida de los hombres
df_male['life_expectancy'] -= df_male['sex'] * 6
df_male['life_expectancy'] -= df_male['smoker'] * 7
df_male['life_expectancy'] += df_male['regular_ex'] * 6
df_male['life_expectancy'] -= df_male['age']
df_male['life_expectancy'] -= df_male['diabetes'] *2
df_male['life_expectancy'] -= (df_male['hereditary_diseases'] == 'Epilepsy') * 6
df_male['life_expectancy'] -= (df_male['hereditary_diseases'] == 'Arthritis') * 4
df_male['life_expectancy'] -= (df_male['hereditary_diseases'] == 'HeartDisease') * 6
df_male['life_expectancy'] -= (df_male['hereditary_diseases'] == 'Cancer') * 12
df_male['life_expectancy'] -= (df_male['hereditary_diseases'] == 'High BP') * 6

df_male['life_expectancy'] -= (df_male['intervals_bmi'] == 'Sobrepeso') * 3
df_male['life_expectancy'] -= (df_male['intervals_bmi'] == 'Obsidad grado 1') * 5
df_male['life_expectancy'] -= (df_male['intervals_bmi'] == 'Obsidad grado 2') * 7
df_male['life_expectancy'] -= (df_male['intervals_bmi'] == 'Obsidad grado 3') * 9


def adjust_life_expectancy(value):
    if value <= 0:
        return 1
    else:
        return value
    
df_male['life_expectancy'] -= (df_male['bmi'] - 40) * 0.75


# Aplicar la función a la columna 'life_expectancy'
df_male['life_expectancy'] = df_male['life_expectancy'].apply(lambda x: adjust_life_expectancy(x))

df_male['life_expectancy'] = df_male['life_expectancy'].round(2)


new_df = pd.concat([df_female,df_male])

new_df.to_csv('./Project/Back/BD/datos_arreglados2.csv')
