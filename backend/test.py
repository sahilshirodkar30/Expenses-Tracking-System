from fastapi import FastAPI
from enum import Enum

app = FastAPI()

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

@app.get("/")
def get_result(cuisine: AvailableCuisines):
    return {"items": food_items.get(cuisine.value, [])}



