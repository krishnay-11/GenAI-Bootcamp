*** 01-getting-started
    - Configured a LangChain chat model using Google Gemini.
    - Loaded the API key securely from a `.env` file using `python-dotenv`.
    - Sent the first prompt to the model and displayed the generated response.

*** 02-weather-agent
    File:- main.py
    - AI-powered weather agent built using LangChain and Gemini.
    - Fetches real-time weather data from the OpenWeatherMap API.
    - Automatically detects the user's location using IP-based geolocation.
    - Provides temperature, weather condition, humidity, wind speed, and other details in Celsius.

    File:- main2.py
    # Multiple Conversation Weather Agent
    - AI weather agent built using LangChain, Gemini, and LangGraph.
    - Maintains conversation history using `InMemorySaver` and a thread ID.
    - Supports continuous user interaction until `bye`, `quit`, `exit`, `thanks`, or `ok`.
    
    File:- main3.py
    # Persistent Memory Weather Agent
    - AI weather agent built using LangChain, Gemini, and LangGraph.
    - Uses SQLite to persist conversation memory across program sessions.
    - Maintains conversation history using a thread ID for continuous conversations.
    - Uses custom weather and location tools to provide weather information.