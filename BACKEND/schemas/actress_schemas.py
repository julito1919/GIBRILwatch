from pydantic import BaseModel

class Actress(BaseModel):
    id_actress: int
    name: str
    description: str
    country:str
    look: str
    gen: str