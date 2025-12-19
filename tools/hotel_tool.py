import json
from langchain.tools import tool
import os

DATA_PATH = os.path.join("data", "hotels.json")

@tool
def hotel_recommendation_tool(
    city: str,
    max_price: int
) -> dict:
    """
    Recommend the best hotel in a city within budget.
    """

    with open(DATA_PATH, "r") as f:
        hotels = json.load(f)

    # Filter by city & price
    filtered = [
        h for h in hotels
        if h.get("city", "").lower() == city.lower()
        and h.get("price_per_night", 0) <= max_price
    ]

    if not filtered:
        return {
            "name": "No hotel found",
            "price_per_night": max_price,
            "rating": "N/A"
        }

    # Use rating if present, else default to 3.5
    best = max(
        filtered,
        key=lambda x: x.get("rating", 3.5)
    )

    return {
        "name": best.get("name", "Unknown Hotel"),
        "price_per_night": best.get("price_per_night", max_price),
        "rating": best.get("rating", "N/A")
    }
