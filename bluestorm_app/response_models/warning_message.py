from pydantic import BaseModel


class WarningMessage(BaseModel):
    message: str
