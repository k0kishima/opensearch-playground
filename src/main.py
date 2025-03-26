from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/ping")
def good_ping():
    return {"pong": True}

app = FastAPI()
app.include_router(router)
