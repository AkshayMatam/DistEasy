from fastapi import FastAPI
from routers.product_router import router as product_router

app = FastAPI(title="DistEasy API")


@app.get("/")
def home():
    return {
        "message": "Welcome to DistEasy Backend"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }


app.include_router(product_router)