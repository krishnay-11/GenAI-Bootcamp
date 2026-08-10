import base64
import mimetypes
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

image_path = "images/img_3.png"
mime_type, _ = mimetypes.guess_type(image_path)

with open(image_path, 'rb') as file:
    raw_binary = file.read()
    base64_bytes = base64.b64encode(raw_binary)
    image_base64 = base64_bytes.decode("utf-8")
    print(type(image_base64))

model = init_chat_model("gemini-3.1-flash-lite", model_provider="google_genai")

message = [{
    "role": "user",
    "content": [
        {"type": "text", "text": "Describe what you see in this image."},
        {"type": "image", "base64": image_base64, "mime_type": mime_type}
    ]
}]

response = model.invoke(message)
print(response.text)