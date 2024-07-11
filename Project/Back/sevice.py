from Project.Back.predictor import predictor_model
from Project.Back.recomend import recomendator
from Project.Back.request import request_user
import numpy as np

from Project.Back.response import response_user

class servicio():
    
    @classmethod
    def generarResponse(cls, user: request_user):
        try:
            user.imc = user.peso/(user.altura**2)
            user.intervalo_imc = servicio.sacar_intervalos(user.imc)
            pred = np.round(predictor_model.predecir(user),2)
            recomend = recomendator.generar_recomendaciones(user)
            response = response_user(recomendaciones=recomend,prediccion=pred)
            
            return response
        except Exception as e:
            return False
        
        
        
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
