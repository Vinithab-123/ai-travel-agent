import json
from langchain.tools import tool

@tool
def places_discovery_tool(city: str, place_type: str = None) -> list:
    """
    Reads places.json, recommends attractions based on type & rating.
    """
    with open("data/places.json", "r") as f:
        places = json.load(f)

    filtered = [
        p for p in places
        if p["city"].lower() == city.lower()
    ]

    if place_type:
        filtered = [
            p for p in filtered
            if p["type"].lower() == place_type.lower()
        ]

    filtered.sort(key=lambda x: x["rating"], reverse=True)

    return filtered[:5]
