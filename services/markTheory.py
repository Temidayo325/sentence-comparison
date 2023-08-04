from services.sentencecompare import Sentencecomparison
from services.listcompare import Listcomparison

from model.model import TheoryEndpointPayload
from model.model import Theory

compareSentence = Sentencecomparison()
compareList = Listcomparison()

class MarkTheory:
        def __init__(self):
                self.finalMark: int = 0

        def mark(self, request : TheoryEndpointPayload):
                for option in request.payload:
                        if option.answer_type == "word" :
                                self.finalMark += compareSentence.compareExplanation(option)
                        
                        if option.answer_type == 'list' :
                                self.finalMark += compareList.compareList(option)
                
                return {"finalScore": self.finalMark, "student_id": request.student_id, "course_id": request.course_id}