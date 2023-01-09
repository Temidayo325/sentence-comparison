import sys
sys.path.append(sys.path[0] + "/..")

from model.model import Listed 
from sentence_transformers import SentenceTransformer, util



model = SentenceTransformer('all-MiniLM-L6-v2')


class Listcomparison:
    def __init__(self):
        self.final_values: int = 0


    def compareList(self, listType: Listed):
        destring_scheme: list = listType.scheme
        destring_answer: list = listType.answer
        scheme_embedding = model.encode(destring_scheme, convert_to_tensor=True)
        answer_embedding = model.encode(destring_answer, convert_to_tensor=True)
        cosine_scores = util.cos_sim(scheme_embedding, answer_embedding)
        values: list = []
        for answer in cosine_scores:
            values.append(max(answer))
        for final in destring_answer:
            self.final_values = float(max(values) * int(listType.mark))
            values.remove(max(values))
        return {"final_score": self.final_values}


