# VitaPredict
Calcula la Esperanza de Vida 


Mejora la velocidad de respuesta y el consumo de recursos aprox 40% de la version 1.0

Primeramente agregando mas recomendaciones personalizadas , teniendo en cuenta los datos del usuario agregando igual una barra de comentarios donde el usuario puede agregar manualmente mejorar o recomendaciones para la fase beta tenemos que probar y retroalimentar el programa , manda un archivo txt donde lo almacenara en descarga y podrás visualizar o imprimir los datos .

Arquitectura:

![alt text](image.png)

Proceso:

-Primeros conseguimos un dataset en internet sobre personas que solicitaban seguros en US y nos informamos de que datos eran relvantes y como estos influian en nuestro target (la esperanza de vida)

![alt text](image-1.png)

-Luego hicimos la limpieza de datos y creacion de columnas calculadas apartir de los datos conseguidos

![alt text](image-2.png)

-Nuestro control de excepciones sera enfocado a la parte de la api aun no terminada

-En nuestro caso usamos un modelo de regresion por el comportamiento de los datos que tienen una clara correlacion de pearson

-Estadisticos:
![alt text](expectativa_vida_diabetes.png)
![alt text](expectativa_vida_fumadores.png)
![alt text](expectativa_vida_peso.png)
![alt text](promedio_bmi_por_edad_intervalos.png)

-Nuestra metrica de evaluacion fue la precision del modelo

Funcionalidades extras:

-Un front con interfaz de usuario
-Modulo de recomendacion en base a los datos del paciente
-Modulo de entrega de las recomendaciones por correo


Arquitectura del projecto:

primero tenemos un modulo llamado main que es el que se deve llamar mediante el siguiente comando para subir el servidor: uvicorn Project.Back.main:app --reload. Este modulo es el que contiene el controlador y utiliza un modulo llamado "service"

service: service es un modulo que simula un servicio de una arquitectura en capas. Este se encarga de generar lo que el controlador debe devolver. Para esto utiliza otros modulos aledaños como "predictor_model" que es el encargado de comunicarse con el modelo y devolver la prediccion, "recomendator" que es el encargado de generar las recomendaciones y advertencias y utiliza una clase llamada response_user que hereda de pydantic el "BaseModel" para devolverlo por el controlador