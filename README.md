# 🧳 AI Travel Planning Assistant

An intelligent, agent-based travel planning system built using **LangChain**, **LangGraph**, and **Streamlit**. The assistant understands user travel queries, calls specialized tools (flights, hotels, places, weather, budget), and generates a **structured, day-wise travel plan**.

---

## 🚀 Features

* 🧠 **LLM-powered Agent** (LangChain + LangGraph)
* ✈️ Flight recommendation (cheapest / suitable option)
* 🏨 Hotel recommendation based on city & budget
* 📍 Tourist place discovery
* 🌦️ Live weather data (Open-Meteo API)
* 💰 Budget estimation
* 🗓️ Day-wise itinerary generation
* 🖥️ Interactive **Streamlit UI**
* 📦 Clean, structured JSON + formatted output

---

## 🏗️ Architecture Overview

```
ai-travel-agent/
│
├── ui.py                  # Streamlit UI
├── app.py                 # Entry / experiments
├── graph/
│   └── travel_graph.py    # LangGraph agent workflow
│
├── tools/                 # LangChain tools
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── places_tool.py
│   ├── weather.py
│   └── budget_tool.py
│
├── data/                  # Static datasets
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
│
├── utils/
│   └── formatter.py       # Final output formatting
│
├── Output/                # Sample outputs (optional)
├── requirements.txt
└── README.md
```

---

## 🔧 Tools Implemented (Step 2)

### 1️⃣ Flight Search Tool

* Reads `flights.json`
* Filters by source → destination
* Suggests best flight

### 2️⃣ Hotel Recommendation Tool

* Reads `hotels.json`
* Filters by city & budget
* Returns best available hotel

### 3️⃣ Places Discovery Tool

* Reads `places.json`
* Recommends popular attractions

### 4️⃣ Weather Lookup Tool

* Uses **Open-Meteo API** (no API key required)
* Returns current temperature & wind speed

### 5️⃣ Budget Estimation Tool

* Combines flight + hotel + food cost
* Returns total estimated budget

---

## 🤖 Agent Responsibilities (Step 3)

The LangGraph agent:

* Understands the user query
* Decides which tools to call
* Executes tools in sequence
* Aggregates results
* Generates a structured travel plan

---

## 📤 Final Output Structure (Step 4)

The system produces:

* Trip Summary
* Flight Selected
* Hotel Recommendation
* Day-wise Itinerary
* Weather Information
* Budget Breakdown

Example format:

```
Your 3-Day Trip to Goa
Flight Selected: Go First (₹5356)
Hotel: Comfort Suites (₹2828/night)
Weather: 27°C, light breeze
Itinerary:
 Day 1: Sightseeing
 Day 2: Local attractions
 Day 3: Relax & return
Total Cost: ₹16,840
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit app

```bash
streamlit run ui.py
```

---

## 🧪 Sample Input

* Source: Bangalore
* Destination: Goa
* Days: 3
* Hotel Budget: ₹3000/night

## ✅ Sample Output

* Structured JSON travel plan
* Human-readable formatted plan

---

## 📌 Technologies Used

* Python
* Streamlit
* LangChain
* LangGraph
* OpenAI GPT models
* Open-Meteo API

---

## 🎯 Project Status

✅ Completed end-to-end
✅ Ready for GitHub submission
✅ Interview-ready project

---

## 🙌 Author

**Vinitha B**
GitHub: [https://github.com/Vinithab-123](https://github.com/Vinithab-123)

---

⭐ If you like this project, give it a star on GitHub!
