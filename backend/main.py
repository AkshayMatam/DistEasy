from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.product_router import router as product_router

app = FastAPI(title="DistEasy API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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