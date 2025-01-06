from pydantic import BaseModel

class SearchQuery(BaseModel):
    question: str
    size: int = 10
