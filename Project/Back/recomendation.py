from pydantic import BaseModel
from typing import List

class recomendation(BaseModel):
    recomendaciones: List[str]
    advertencias: List[str]
