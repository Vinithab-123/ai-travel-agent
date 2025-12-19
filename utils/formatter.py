def format_travel_plan(data: dict) -> str:
    """
    Converts structured travel plan JSON into human-readable format
    """

    trip = data["trip_summary"]
    budget = data["budget"]

    output = []
    output.append(f"🧳 Your {trip['days']}-Day Trip to {trip['destination']}\n")

    # Flights
    output.append("✈️ Flight Selected:")
    for f in data["flights"]:
        output.append(
            f"- {f['airline']} (₹{f['price']}) – Departs at {f['departure_time']}"
        )

    # Hotel
    hotel = data["hotel"]
    output.append("\n🏨 Hotel:")
    output.append(
        f"- ₹{hotel['price_per_night']} per night | Total: ₹{hotel['total_cost']}"
    )

    # Weather
    output.append("\n🌤 Weather:")
    for i, w in enumerate(data["weather"], start=1):
        temp = w.get("temperature", "N/A")
        wind = w.get("windspeed", "")
        output.append(f"- Day {i}: {temp} {wind}")

    # Itinerary
    output.append("\n🗺 Itinerary:")
    for day, plan in data["itinerary"].items():
        output.append(f"{day.replace('_', ' ').title()}: {plan}")

    # Budget
    output.append("\n💰 Budget Breakdown:")
    output.append(f"- Hotel: ₹{budget['hotel']}")
    output.append(f"- Food: ₹{budget['food']}")
    output.append(f"- Travel: ₹{budget['travel']}")
    output.append("-" * 30)
    output.append(f"Total Cost: ₹{budget['total']}")

    return "\n".join(output)
