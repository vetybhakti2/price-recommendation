from fastapi import FastAPI
from app.services.price_service import recommend_price

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Price Recommendation API!"}

@app.get("/recommend/{product_name}")
def recommend_product_price(product_name: str):
    result = recommend_price(product_name)
    return result