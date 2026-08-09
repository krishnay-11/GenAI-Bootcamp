from langchain.chat_models import init_chat_model


model = init_chat_model(
    model='qwen3:1.7b',
    model_provider="ollama"
)

response = model.invoke("How to be healthy?")
print(response.text)