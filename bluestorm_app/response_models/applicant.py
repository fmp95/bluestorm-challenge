from pydantic import BaseModel


class Applicant(BaseModel):
    name: str