from langchain.tools import tool

@tool
def budget_estimation_tool(
    flight_price: int,
    hotel_price_per_night: int,
    days: int,
    daily_expense: int = 1000
) -> dict:
    """
    Calculates total trip budget.
    """
    hotel_cost = hotel_price_per_night * days
    food_travel = daily_expense * days
    total = flight_price + hotel_cost + food_travel

    return {
        "flight": flight_price,
        "hotel": hotel_cost,
        "food": food_travel,
        "total": total
    }
