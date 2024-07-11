from Project.Back.recomendation import recomendation
from Project.Back.request import request_user


class recomendator():
    
    @classmethod
    def generar_recomendaciones(cls,user: request_user):
        enfermedades_es = {
                        "Ninguna": ([]),
                        "Enfermedad cardíaca": (["Seguir una dieta saludable", "Ejercicio regular", "Evitar el tabaco", "Tomar medicamentos según las indicaciones"]),
                        "Hipertensión": (["Reducir la ingesta de sal", "Ejercicio regular", "Controlar el estrés", "Tomar medicamentos según las indicaciones"]),
                        "Cáncer": (["Seguir las recomendaciones del oncólogo", "Mantener un estilo de vida saludable", "Evitar el tabaco y el alcohol"]),
                        "Enfermedad pulmonar": (["Evitar el tabaco", "Hacer ejercicios respiratorios", "Seguir las indicaciones del neumólogo"]),
                        "Enfermedad renal crónica": (["Seguir una dieta baja en sal y proteínas", "Mantener un control regular con el nefrólogo", "Tomar medicamentos según las indicaciones"]),
                        "Obesidad": (["Seguir una dieta equilibrada", "Realizar actividad física regular", "Consultar con un nutricionista"]),
                        "Enfermedad hepática": (["Evitar el alcohol", "Mantener una dieta saludable", "Seguir las indicaciones del hepatólogo"]),
                        "Enfermedad neurodegenerativa": (["Realizar ejercicios mentales y físicos", "Seguir una dieta saludable", "Mantener el apoyo social y emocional"]),
                        "VIH/SIDA": (["Seguir el tratamiento antirretroviral", "Mantener un estilo de vida saludable", "Evitar conductas de riesgo"]),
                        "Artritis": (["Realizar ejercicios de bajo impacto", "Seguir las indicaciones del reumatólogo", "Mantener un peso saludable"])
                    }
        recomendacion = list(enfermedades_es[user.enfermedad])
        advertencias = []
        
        if (user.diabetes and user.fumador) or (user.diabetes and user.edad > 40):
            advertencias.append('Debe tener mucho cuidado con su salud, debido a que las personas diabeticas son mas propensas a contraer cancer y el mismo a crecer muy rapidamente. Le recomendamos muy encarecidamente que cuide muy bien de su salud')
        elif user.fumador:
            advertencias.append('Le recomendamos que deje de fumar, pues, el 90% de los canceres de pulmon son provocados por el consumo de cigarrillos')

        if user.diabetes and user.intervalo_imc == 'Bajo peso':
            advertencias.append('Deberia ir lo antes posible a su medico de cabecera, puesto que, usted presenta un bajo peso lo cual no es favorable con su condicion diabetico. Estas dos caracteristicas juntas nos indican que su diabetes no esta siendo controlada debidamente. Por favor acuda a un medico')
            
        if user.intervalo_imc == 'Sobrepeso':
            advertencias.append('Deberia recomendamos llevar una vida mas saludable y asi mejorar su calidad de vida. Usted presenta un sobrepeso que a la larga le puede traer dificultades en su vida diaria, como cansancio, dolor en las articulaciones e ineficiencia sexual')
        elif user.intervalo_imc == 'Obesidad grado 1' or user.intervalo_imc == 'Obesidad grado 2' or user.intervalo_imc == 'Obesidad grado 3':
            advertencias.append(f'Deberia intentar bajar de peso lo antes posible. Usted presenta {user.intervalo_imc} lo cual afecta muy negativamente a su calidad de vida y a su salud. Por favor acuda con un profesional de ser necesario')
        
        if not user.ejercicio:
            advertencias.append('Le recomendamos hacer actividad fisica. Esta demostrado cientificamente que de 3 a 5 horas de caminata a la semana suponen un impacto positivo en la salud de una persona')
        
        if (not user.sexo and user.diabetes):
            advertencias.append('Le recomendamos realizar sus estudios rutinarios 2 veces al año en lugar de 1. Esta demostrado que las mujeres les afecta mas negativamente la diabetes que a los hombres, asi que le recomendamos hacerse una mamografia cada 6 meses para prevenir cancer de mama, pues, las personas diabeticas son mas propensas a contraer cancer')
        
        recomend = recomendation(recomendaciones=recomendacion,advertencias=advertencias)
        return recomend

