from dotenv import load_dotenv
load_dotenv()

import json
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from graph.travel_graph import travel_graph


# -----------------------------
# USER QUERY
# -----------------------------
user_query = """
Plan a 3-day trip from Bangalore to Goa.
Hotel budget 3000 per night.
Include flights, places, weather, and total budget.
"""


# -----------------------------
# RUN AGENT
# -----------------------------
agent_result = travel_graph.invoke({
    "messages": [HumanMessage(content=user_query)]
})

raw_output = agent_result["messages"][-1].content


# -----------------------------
# FORMAT OUTPUT TO JSON
# -----------------------------
formatter_llm = ChatOpenAI(model="gpt-4o-mini")

format_prompt = f"""
Convert the following travel plan into STRICT JSON.

Schema:
{{
  "flight": {{
    "airline": "",
    "price": "",
    "departure_time": ""
  }},
  "hotel": {{
    "name": "",
    "price_per_night": "",
    "total_cost": ""
  }},
  "places": [],
  "weather": {{
    "day_1": "",
    "day_2": "",
    "day_3": ""
  }},
  "budget": {{
    "flight": "",
    "hotel": "",
    "food": "",
    "total": ""
  }}
}}

Rules:
- Output ONLY JSON
- No markdown
- No explanation

TEXT:
{raw_output}
"""

json_response = formatter_llm.invoke([
    SystemMessage(content="You convert text to clean JSON."),
    HumanMessage(content=format_prompt)
])

structured_data = json.loads(json_response.content)


# -----------------------------
# DAY-WISE ITINERARY GENERATION
# -----------------------------
itinerary_prompt = f"""
You are a travel planner.

Using the following details:
City: Goa
Places: {structured_data["places"]}
Trip Duration: 3 days

Create a realistic DAY-WISE itinerary.

Rules:
- Day 1: Arrival + light sightseeing
- Day 2: Full exploration
- Day 3: Relaxation + return
- Keep it practical
- Output STRICT JSON only

Format:
{{
  "day_1": "",
  "day_2": "",
  "day_3": ""
}}
"""

itinerary_response = formatter_llm.invoke([
    SystemMessage(content="You generate structured travel itineraries."),
    HumanMessage(content=itinerary_prompt)
])

structured_data["itinerary"] = json.loads(itinerary_response.content)


# -----------------------------
# FINAL OUTPUT
# -----------------------------
print("\n🧳 FINAL STRUCTURED TRAVEL PLAN\n")
print(json.dumps(structured_data, indent=2))
