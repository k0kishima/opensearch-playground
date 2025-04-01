from fastapi import APIRouter, Query
from typing import List
from src.companies.schemas import CompanyResponse
from src.companies.service import search_companies

router = APIRouter(prefix="/api/v1/companies", tags=["Companies"])

@router.get("/search", response_model=List[CompanyResponse])
async def search(keyword: str = Query(..., description="Search keyword")):
    return await search_companies(keyword)
