from fastapi import FastAPI
from src.companies.router import router as companies_router

app = FastAPI()
app.include_router(companies_router)
