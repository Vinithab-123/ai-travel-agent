import sys
import os
import json

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# --------------------------------------------------
# PATH SETUP
# --------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

from graph.travel_graph import travel_graph

# --------------------------------------------------
# ENV SETUP
# --------------------------------------------------
load_dotenv()

st.set_page_config(
    page_title="AI Travel Planning Assistant",
    layout="wide"
)

st.title("🧳 AI Travel Planning Assistant")

# --------------------------------------------------
# USER INPUTS
# --------------------------------------------------
st.subheader("Trip Details")

source = st.text_input("Source City", "Bangalore")
destination = st.text_input("Destination City", "Goa")
days = st.number_input("Number of Days", min_value=1, max_value=10, value=3)
hotel_budget = st.number_input("Hotel Budget per Night (₹)", value=3000)

# --------------------------------------------------
# BUTTON ACTION
# --------------------------------------------------
if st.button("Generate Travel Plan"):

    with st.spinner("🧠 AI agent is planning your trip..."):

        result = travel_graph.invoke({
            "messages": [
                HumanMessage(
                    content=f"Plan a {days}-day trip from {source} to {destination} "
                            f"with hotel budget {hotel_budget} per night."
                )
            ]
        })

    # --------------------------------------------------
    # EXTRACT TOOL OUTPUTS SAFELY
    # --------------------------------------------------
    messages = result["messages"]

    flight = None
    hotel = None
    budget = None

    for msg in messages:
        if msg.__class__.__name__ == "ToolMessage":
            try:
                data = json.loads(msg.content)
            except:
                continue

            if msg.name == "flight_search_tool":
                flight = data

            elif msg.name == "hotel_recommendation_tool":
                hotel = data

            elif msg.name == "budget_estimation_tool":
                budget = data

    # --------------------------------------------------
    # BUILD FINAL OUTPUT (STEP 4)
    # --------------------------------------------------
    final_output = {
        "trip_summary": {
            "source": source,
            "destination": destination,
            "days": days
        },
        "flight_selected": flight,
        "hotel_recommendation": hotel,
        "day_wise_itinerary": {
            f"Day {i+1}": "Sightseeing and leisure activities"
            for i in range(days)
        },
        "weather": "Provided via weather tool (if enabled)",
        "budget_breakdown": budget
    }

    # --------------------------------------------------
    # DISPLAY OUTPUT
    # --------------------------------------------------
    st.success("✅ Travel Plan Generated Successfully")

    st.subheader("📄 Final Travel Plan")
    st.json(final_output)
