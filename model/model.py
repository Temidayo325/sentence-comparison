from pydantic import BaseModel

class Sentence(BaseModel):
    scheme: str
    answer: str
    mark: int


class Listed(BaseModel):
    scheme: list
    answer: list
    mark: int

