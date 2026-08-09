import requests

API_URL = "http://localhost:5000"

url = f"{API_URL}/chat"

history = []

while True:
    user_input = input("You: ")
    history.append({"role": "user", "content": user_input})
    response = requests.post(
        url,
        json={"messages": history})

    assistant_message = response.json()['message']
    history.append(assistant_message)
    print(assistant_message['content'])