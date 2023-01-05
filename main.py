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
    return {"scheme": sentence.scheme, "answer": sentence.answer, "score": tryToMark}