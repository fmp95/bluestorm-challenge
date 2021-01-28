from time import time

from fastapi import APIRouter

from ..response_models import Medications
from ..common import MedicationSearcher
from ..logs import api_logs

router = APIRouter()


@router.get("/search/{medication}", response_model=Medications)
def search_medication(medication: str):

    start_time = time()

    searcher = MedicationSearcher()

    results = searcher.search(medication)

    api_logs.info(
        f"Request processed in {time() - start_time:.2f} seconds | Endpoint: /search/ | Parameter: {medication} | Results: {len(results)}"
    )

    return {"medications": results}