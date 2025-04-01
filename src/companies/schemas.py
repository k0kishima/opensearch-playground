from pydantic import BaseModel
from typing import List


class CompanyResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    is_public: bool
    synonym: List[str]
