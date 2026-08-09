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

    File:- main4.py
    # PostgreSQL Persistent Memory Weather Agent

    - AI weather agent built using LangChain, Gemini, and LangGraph.
    - Uses Supabase PostgreSQL with PostgresSaver for persistent memory.
    - Maintains conversation history using a thread ID across sessions.
    - Uses custom weather and location tools to provide weather information.

    File:- main_flask.py

    - Implements the Flask backend and handles application routes such as `/`, `/send`, and `/clear`.
    - Manages user sessions, conversation `thread_id`, chat history, and user location.
    - Receives user messages and browser latitude/longitude and passes them to the AI agent.
    - Processes the agent response and sends the conversation data to the frontend.

    File:- flask_agent.py

    - Creates the AI weather agent using Google Gemini, LangChain, and LangGraph.
    - Implements the `get_weather()` tool to retrieve weather data from the OpenWeatherMap API.
    - Implements the `get_location()` tool to convert the user's coordinates into their city using Nominatim.
    - Uses SQLite checkpointing and a system prompt to maintain conversations and control agent tool usage.

    File:- chat.html in templates folder

    - Provides the frontend chat interface for interacting with the weather assistant.
    - Displays user and AI messages dynamically using Jinja2.
    - Uses the browser Geolocation API to capture the user's latitude and longitude.
    - Sends user messages and location data to Flask and provides a New Conversation option.

*** 03-self-hostable-models

    - Configured a LangChain chat model using Ollama.
    - Used Qwen3 1.7B as a self-hostable model running locally.
    - Invoked the model using `model.invoke()` and displayed the generated response.

*** 04-self-llm-service
    File:- server.py, client.py

    - Created a self-hosted LLM service using Flask, LangChain, and Ollama.
    - Used Ollama to run the Qwen3 1.7B model locally without relying on an external LLM API.
    - Exposed a `/chat` API endpoint to process user messages and generate responses using the local model.
    - Built a client using `requests` to communicate with the Flask service and maintain chat history.

*** 05-structured-output-llm
    File:- email_agent.py, recipe_generator.py

      #email_agent.py
    - Created an AI email agent using LangChain, Google Gemini, Pydantic, and environment variables.
    - Used the Gemini gemini-3.1-flash-lite model to understand user requests and generate appropriate email content.
    - Created a custom send_email tool that the agent can use when the user requests an email to be sent.
    - Used Pydantic structured output to return the recipient, subject, body, status, and summary in a defined format.

      #recipe_generator.py
    - Created a structured recipe generator using LangChain, Google Gemini, Pydantic, and environment variables.
    - Used the Gemini gemini-3.1-flash-lite model to identify ingredients and suggest recipes based on user input.
    - Defined Pydantic models to structure recipe information including name, description, preparation time, ingredients, and recipes.
    - Used with_structured_output() to ensure the LLM returns the recipe response in the predefined structured format.    

*** 06-spreadsheet-automation
    File:- spreadsheet_summary.py

    - Fetches data from Google Spreadsheet using the Google Sheets API and identifies newly added rows using `last_row.txt`.
    - Uses LangChain with a Google AI model to summarize the newly added spreadsheet data.
    - Sends the generated summary through Gmail SMTP to the configured recipient.
    - Uses `.env` to store API keys and email details, while `last_row.txt` tracks previously processed rows.
