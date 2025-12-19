from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

# ✅ IMPORT USING ACTUAL FILENAMES
from tools.flight_tool import flight_search_tool
from tools.hotel_tool import hotel_recommendation_tool
from tools.places_tool import places_discovery_tool
from tools.budget_tool import budget_estimation_tool
from tools.weather import get_weather



# ---- LLM ----
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# ---- TOOLS ----
tools = [
    flight_search_tool,
    hotel_recommendation_tool,
    places_discovery_tool,
    budget_estimation_tool,
    get_weather
]

# ---- AGENT ----
travel_graph = create_react_agent(
    model=llm,
    tools=tools
)
