from fastapi import APIRouter

from response_models import Medications
from common import MedicationSearcher

router = APIRouter()


@router.get("/search/{medication}", response_model=Medications)
def search_medication(medication: str):

    searcher = MedicationSearcher()

    return {"medications": searcher.search(medication)}