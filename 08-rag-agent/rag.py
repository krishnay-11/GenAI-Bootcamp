from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    DirectoryLoader,
    TextLoader
)

load_dotenv()

directory = "Documents"

# Invoke the LLM
llm = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')


# Load Documents
pdf_loader = PyPDFDirectoryLoader(directory)
pdf_docs = pdf_loader.load()

text_loader = DirectoryLoader(
    directory,
    glob="**/*.txt",
    loader_cls=TextLoader
)

text_docs = text_loader.load()

docs = pdf_docs + text_docs


# Creating embeddings and vector store
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = InMemoryVectorStore(embeddings)

vector_store.add_documents(docs)


# Chat loop
while True:

    # Get user query
    user_query = input('Enter your query: ')

    # Exit condition
    if user_query.lower() in ['ok','exit', 'quit', 'thank you','thanks']:
        break

    # Retrieve relevant documents
    retrieved_docs = vector_store.similarity_search(
        user_query,
        k=5
    )

    # Create context from retrieved documents
    context = "\n".join(
        doc.page_content for doc in retrieved_docs
    )

    system_prompt = f"""
    You are a helpful assistant that answers questions about these documents:

    {context}
    """
    messages = [
        SystemMessage(content=system_prompt)
    ]

    messages.append(
        HumanMessage(content=user_query)
    )

    response = llm.invoke(messages)

    print(response.content[0]["text"])