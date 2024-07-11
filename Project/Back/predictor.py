from Project.Back.request import request_user
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

class predictor_model():
    
    @classmethod
    def predecir(cls, user: request_user):
        try:
            # Cargar el modelo y el encoder desde los archivos pickle
            with open('./Project/Back/BD/random_forest_model.pkl', 'rb') as f:  
                model = pickle.load(f)
            with open('./Project/Back/BD/encoder_imc.pkl', 'rb') as f:  
                le = pickle.load(f)
                    
            

            
            # Transformar el intervalo usando el encoder cargado
            intervalo_transformado = le.transform([user.intervalo_imc])
            
            # Preparar los datos para la predicción
            datos = [
                user.edad,
                user.sexo,
                user.peso,
                user.imc,
                user.fumador,
                user.diabetes,
                user.ejercicio,
                intervalo_transformado[0]
            ]
            datos = np.array(datos).reshape(1, -1)  # Asegurar que los datos tengan la forma correcta
            
            # Realizar la predicción
            prediction = model.predict(datos)
            return prediction[0]
        except Exception as e:
            print(f"Error: {e}")
            return str(e)
    
    @classmethod
    def sacar_intervalos(cls, imc: float):
        if imc < 18.5:
            return 'Bajo peso'
        elif imc < 25:
            return 'Adecuado'
        elif imc < 30:
            return 'Sobrepeso'
        elif imc < 35:
            return 'Obesidad grado 1'
        elif imc < 40:
            return 'Obesidad grado 2'
        else:
            return 'Obesidad grado 3'
