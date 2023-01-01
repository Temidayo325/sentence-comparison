from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Sentence(BaseModel):
    scheme: str
    answer: str
    mark: int
@app.post('/compare/explaination')
def compareExplaination(sentence: Sentence):
    return sentence