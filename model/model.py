from pydantic import BaseModel
from typing import Union
class Sentence(BaseModel):
    scheme: str
    answer: str
    mark: int


class Listed(BaseModel):
    scheme: list
    answer: list
    mark: int

class Theory(BaseModel):
    answer : Union[str, list]
    answer_type : str
    scheme : Union[str, list]
    marks : int

class TheoryEndpointPayload(BaseModel):
    student_id : str
    course_id : str
    payload: list[Theory]