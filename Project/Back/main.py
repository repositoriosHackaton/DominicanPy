from fastapi import FastAPI
from Project.Back.request import request_user
from Project.Back.sevice import servicio
app = FastAPI()

@app.post("/predictor/")
def predictor(user: request_user):
    try:
        return servicio.generarResponse(user)
    except Exception as e:
        return e