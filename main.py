from sentence_transformers import SentenceTransformer, util
from fastapi import FastAPI
from pydantic import BaseModel

model = SentenceTransformer('all-MiniLM-L6-v2')

app = FastAPI()


class Sentence(BaseModel):
    scheme: str
    answer: str
    mark: int

@app.post('/compare/explaination')
def compareExplaination(sentence: Sentence):
    tryToMark : int = 0
    scheme_embedding = model.encode(sentence.scheme, convert_to_tensor=True)
    answer_embedding = model.encode(sentence.answer, convert_to_tensor=True)
    cosine_scores = util.cos_sim(scheme_embedding, answer_embedding)
    for index in cosine_scores:
        for value in index:
            tryToMark = float(value) * sentence.mark
    return {"score": tryToMark}


class Listed(BaseModel):
    scheme: list
    answer: list
    mark: int
@app.post('/compare/list')
def compareList(sentence: Listed):
    destring_scheme: list = sentence.scheme
    destring_answer: list = sentence.answer
    scheme_embedding = model.encode(destring_scheme, convert_to_tensor=True)
    answer_embedding = model.encode(destring_answer, convert_to_tensor=True)
    cosine_scores = util.cos_sim(scheme_embedding, answer_embedding)
    values: list = []
    final_values: int = 0
    for answer in cosine_scores:
        values.append(max(answer))
    for final in destring_answer:
        final_values += float(max(values) * int(sentence.mark))
        values.remove(max(values))
    return {"final_score": final_values}