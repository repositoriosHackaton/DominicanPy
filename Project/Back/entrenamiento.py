import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, ShuffleSplit
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('./Project/Back/BD/datos_arreglados2.csv')

# Conversion a numerico los alfanumericos
le = LabelEncoder()


encoded_imc = le.fit_transform(df['intervals_bmi'])
df['intervals_bmi'] = encoded_imc

# Guardar el modelo entrenado
with open('./Project/Back/BD/encoder_imc.pkl', 'wb') as f:
    pickle.dump(le, f)


#Particion de los datos de entranamiento
X= df.drop(columns=['life_expectancy','hereditary_diseases','bloodpressure','Unnamed: 0'])
y = df['life_expectancy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# #Creacion del mejor modelo
# cv_sets = ShuffleSplit(n_splits = 10, test_size = 0.2, random_state = 0)
# params_rf = {'n_estimators':np.array(range(50,1000,100)), 'max_features': [0.5,'auto', 'sqrt','log2'], 'min_samples_leaf': [1,2,4]}
# grid_search = GridSearchCV(estimator= RandomForestRegressor(random_state=7), param_grid=params_rf, scoring='r2', cv=cv_sets, verbose= 3, n_jobs=-1)
# grid_search.fit(X_train, y_train)
# model = grid_search.best_estimator_

#----------------Este codigo de aqui es para reentrenar el modelo ya existente para no tener que crear el modelo otra vez, sino que aprende de nuevos datos
with open('./Project/Back/BD/random_forest_model.pkl', 'rb') as f:  # Replace 'model.pkl' with the actual filename
    model = pickle.load(f)


#Entrenamiento del modelo    
model.fit(X_train, y_train)
print(model.predict(X_train))
#Porcentaje de exito del modelo
print(model.score(X_test,y_test))
    
# Guardar el modelo entrenado
with open('./Project/Back/BD/random_forest_model.pkl', 'wb') as f:
    pickle.dump(model, f)


