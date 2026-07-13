from fastapi import FastAPI
import sqlite3

app = FastAPI(title="DistEasy API")

DATABASE = "disteasy.db"


@app.get("/")
def home():
    return {"message": "Welcome to DistEasy Backend"}


@app.get("/health")
def health():
    return {"status": "Running"}


@app.get("/products")
def get_products():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return {"products": products}