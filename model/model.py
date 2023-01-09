from pydantic import BaseModel


class Sentence(BaseModel):
    scheme: str
    answer: str
    mark: int

