import sys
sys.path.append(sys.path[0] + "/..")

# from model.model import Sentence 
from model.model import Theory
from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')


class Sentencecomparison:
    def __init__(self):
        self.tryToMark: int = 0
   
    # def compareExplanation(self, sentence: Sentence):
    def compareExplanation(self, sentence: Theory):
        scheme_embedding = model.encode(sentence.scheme, convert_to_tensor=True)
        answer_embedding = model.encode(sentence.answer, convert_to_tensor=True)
        cosine_scores = util.cos_sim(scheme_embedding, answer_embedding)
        for index in cosine_scores:
            for value in index:
                self.tryToMark += round(float(value) * sentence.marks, 1)
        # return {"scheme": sentence.scheme, "answer": sentence.answer, "score": self.tryToMark}
        return self.tryToMark

    def home(self):
        return {"working": True, "status": 200}