import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent
import os

load_dotenv()

def get_weather(city: str):
    """Get the current weather for a given city."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city,
        "appid":api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_location():
    """Get user's current location."""
    response = requests.get("https://ipapi.co/json/", headers = {'User-agent': 'your-bot 0.1'})
    data = response.json()
    city = data['city']
    country = data.get('country_name')
    return f"{city}, {country}"

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7,
)
system_prompt = """
You are a helpful weather assistant. 
HERE IS YOUR WORKFLOW:
1. If the user asks about weather WITHOUT specifying a location, you MUST:
   - First call get_location() to find their location
   - Then call get_weather(city) with that location
   
2. If the user provides a city, call get_weather(city) directly.

3. Always report temperature in Celsius.

4. Present the weather information including temperature, condition, wind speed, and any other relevant details.
"""
agent = create_agent(
    model=llm,
    tools=[get_weather, get_location],
    system_prompt=system_prompt
)

if __name__ == "__main__":
    user_query = input("Enter your query: ")

    response1 = agent.invoke(
        {"messages": [{'role': 'user',
                       'content':user_query}]})
    print(response1["messages"][-1].content[0]["text"])
