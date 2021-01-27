from pydantic import BaseModel


class Route(BaseModel):
    method: str