"""
Simple prompt and completion with Ollama
"""

from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def get_stream(query):
    for chunks in llm.stream(query):
        print(chunks)

def get_full(query):
    return llm.invoke(query)

query = "Tell me a joke"

# Wait for the full answer
print(get_full(query))

# Stream the answer as it comes in
#print(get_stream(query))
