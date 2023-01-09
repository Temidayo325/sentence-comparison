import sys
import os
sys.path.append(sys.path[0] + "/..")
from dotenv import load_dotenv




from services.sentencecompare import Comparison
from fastapi import FastAPI, APIRouter

load_dotenv('.env')

app = FastAPI()

compare = Comparison()


router = APIRouter()
router.add_api_route(os.getenv("COMPARE_EXPLANATION_ENDPOINT"), endpoint=compare.compareExplanation, methods=["POST"])
app.include_router(router)


