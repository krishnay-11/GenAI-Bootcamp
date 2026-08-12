from pathlib import Path
from pypdf import PdfReader

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()


def load_documents(directory='Documents'):
    documents = []

    for file_path in Path(directory).rglob('*'):
        if file_path.suffix in {'.txt', '.pdf', '.md'}:
            if file_path.suffix == '.pdf':
                reader = PdfReader(file_path)
                content = "\n".join(
                    page.extract_text() for page in reader.pages
                )
            else:
                content = file_path.read_text()

            documents.append({
                'path': str(file_path),
                'content': content
            })

    return documents


def create_context(document_list):
    context = ''

    for doc in document_list:
        context = context + f"{doc['path']}:\n{doc['content']}\n------------\n"

    return context


documents = load_documents()
context = create_context(documents)

system_prompt = f"""
You are a helpful assistant that answers questions about these documents: {context}
"""

messages = [
    SystemMessage(content=system_prompt)
]

llm = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

while True:
    user_query = input('Enter your query: ')
    if user_query.lower() in ['ok','thank you','thanks','exit', 'quit', 'q']:
        print("Exiting...")
        break

    messages.append(HumanMessage(content=user_query))
    response = llm.invoke(messages)

    print(response.content[0]["text"])
    messages.append(response)