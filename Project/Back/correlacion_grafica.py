import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('./Project/Back/BD/datos_arreglados2.csv')

# Conversion a numerico los alfanumericos
le = LabelEncoder()

encoded_hereditary_diseases = le.fit_transform(df['hereditary_diseases'])

df['hereditary_diseases'] = encoded_hereditary_diseases
encoded_imc = le.fit_transform(df['intervals_bmi'])
df['intervals_bmi'] = encoded_imc
plt.figure(figsize=(12,8))
g = sns.heatmap(df.corr(), annot=True)
g.set_xticklabels(g.get_xticklabels(), rotation=75)
plt.show()