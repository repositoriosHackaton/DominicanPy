from pydantic import BaseModel
from typing import Optional

class request_user(BaseModel):
    
    edad: int
    peso: float
    altura: float
    diabetes: bool
    fumador: bool
    enfermedad: str
    ejercicio:bool
    sexo: bool
    imc: Optional[float] = None
    intervalo_imc: Optional[str] = None

