import json
from langchain.tools import tool

@tool
def flight_search_tool(source: str, destination: str) -> dict:
    """
    Reads flights.json, filters by source & destination,
    returns cheapest flight.
    Handles inconsistent key names safely.
    """
    with open("data/flights.json", "r") as f:
        flights = json.load(f)

    normalized = []
    for f in flights:
        flight_source = f.get("source") or f.get("from") or f.get("origin")
        flight_dest = f.get("destination") or f.get("to")
        price = f.get("price") or f.get("cost")

        if not flight_source or not flight_dest or not price:
            continue

        if (
            flight_source.lower() == source.lower()
            and flight_dest.lower() == destination.lower()
        ):
            normalized.append({
                "airline": f.get("airline", "Unknown"),
                "price": price,
                "departure_time": f.get("departure_time", "N/A"),
                "source": flight_source,
                "destination": flight_dest
            })

    if not normalized:
        return {"error": "No flights found"}

    cheapest = min(normalized, key=lambda x: x["price"])
    return cheapest
