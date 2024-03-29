import sys
sys.path.append(sys.path[0] + "/..")

# from model.model import Listed
from model.model import Theory
from sentence_transformers import SentenceTransformer, util



model = SentenceTransformer('all-MiniLM-L6-v2')


class Listcomparison:
    def __init__(self):
        self.final_values: int = 0


    # def compareList(self, listType: Listed):
    def compareList(self, listType: Theory):
        destring_scheme: list = listType.scheme
        destring_answer: list = listType.answer
        scheme_embedding = model.encode(destring_scheme, convert_to_tensor=True)
        answer_embedding = model.encode(destring_answer, convert_to_tensor=True)
        cosine_scores = util.cos_sim(scheme_embedding, answer_embedding)
        values: list = []

        values = [max(answer) for answer in cosine_scores]
        for final in destring_answer:
            self.final_values += round(float(max(values) * int(listType.marks)), 1)
            values.remove(max(values))
        # return {"final_score": self.final_values}
        return self.final_values


