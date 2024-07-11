from fastapi import FastAPI
from Project.Back.request import request_user
from Project.Back.sevice import servicio
app = FastAPI()

@app.post("/prueba/")
def prueba(user: request_user):
    try:
        print('entro')
        return servicio.generarResponse(user)
    except Exception as e:
        return e