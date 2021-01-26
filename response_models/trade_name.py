from pydantic import BaseModel


class TradeName(BaseModel):
    name: str