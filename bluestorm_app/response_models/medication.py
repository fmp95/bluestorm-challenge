from typing import List, Optional

from pydantic import BaseModel

from .ingredient import Ingredient
from .df import DF
from .route import Route
from .trade_name import TradeName
from .applicant import Applicant
from .strength import Strength
from .warning_message import WarningMessage


class Medication(BaseModel):
    ingredients: List[Ingredient]
    dfs: List[DF]
    routes: List[Route]
    trade_names: List[TradeName]
    applicants: List[Applicant]
    strengths: List[Strength]
    warning_messages: Optional[List[WarningMessage]]

    class Config:

        schema_extra = {
            "example": {
                "ingredients": [
                    {"name": "ACETAMINOPHEN"},
                    {"name": "CODEINE PHOSPHATE"},
                ],
                "dfs": [{"method": "TABLET"}],
                "routes": [{"method": "ORAL"}],
                "trade_names": [{"name": "TYLENOL W/ CODEINE"}],
                "applicants": [{"name": "ORTHO MCNEIL PHARM"}],
                "strengths": [{"amount": "325MG"}, {"amount": "7.5MG"}],
                "warning_messages": [
                    {"message": "Federal Register determi…ety or efficacy reasons"}
                ],
            }
        }


class Medications(BaseModel):
    medications: List[Medication]