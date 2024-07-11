from pydantic import BaseModel

from Project.Back.recomendation import recomendation

class response_user(BaseModel):
    recomendaciones: recomendation
    prediccion: float