import sys
import os
sys.path.append(sys.path[0] + "/..")
from dotenv import load_dotenv
import uvicorn




from services.sentencecompare import Sentencecomparison
from services.listcompare import Listcomparison
from services.markTheory import MarkTheory
from fastapi import FastAPI, APIRouter

load_dotenv('.env')

app = FastAPI()

compareSentence = Sentencecomparison()
compareList = Listcomparison()
getAnswer = MarkTheory()

router = APIRouter()

router.add_api_route("/home", endpoint = compareSentence.home, methods=["GET"])

router.add_api_route("/marktheory", endpoint = getAnswer.mark, methods=["POST"])

# router.add_api_route("/explain", endpoint = compareSentence.compareExplanation, methods=["POST"])
router.add_api_route(os.getenv("COMPARE_EXPLANATION_ENDPOINT", "/explain"), 
endpoint = compareSentence.compareExplanation, methods=["POST"])

router.add_api_route(os.getenv("COMPARE_LISTED_ENDPOINT", "/list"), 
endpoint = compareList.compareList, methods=["POST"])

app.include_router(router)


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8500, reload=True)