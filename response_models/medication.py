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


class Medications(BaseModel):
    medications: List[Medication]