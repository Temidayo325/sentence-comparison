import sys
import os
sys.path.append(sys.path[0] + "/..")
from dotenv import load_dotenv




from services.sentencecompare import Sentencecomparison
from services.listcompare import Listcomparison
from fastapi import FastAPI, APIRouter

load_dotenv('.env')

app = FastAPI()

compareSentence = Sentencecomparison()
compareList = Listcomparison()


router = APIRouter()

router.add_api_route(os.getenv("COMPARE_EXPLANATION_ENDPOINT"), 
endpoint = compareSentence.compareExplanation, methods=["POST"])

router.add_api_route(os.getenv("COMPARE_LISTED_ENDPOINT"), 
endpoint = compareList.compareList, methods=["POST"])

app.include_router(router)


