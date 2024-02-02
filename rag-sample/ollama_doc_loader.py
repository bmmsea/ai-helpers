"""
1. Load txt documents from a directory.
2. Use locally running Ollama to create vector embeddings for ChromaDB and persist to disk

Project: https://github.com/bmmsea/ai-helpers
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Change to your directory with documents and the location to persist embeddings
persist_dir = 'embeddings'
doc_dir = 'docs'

# Any Ollama model should work from https://ollama.ai/library
embeddings = OllamaEmbeddings(model='mistral')


def doc_to_embeddings(dir):
    """
    Load txt documents from an input directory, convert to embeddings and persist to disk
    
    Input: Directory
    Output: Doc count
    """
    loader = DirectoryLoader(dir, glob="**/*.txt")
    documents = loader.load()

    # split it into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)

    # create the open-source embedding function
    db = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_dir)
    
    return db._collection.count()


if __name__ == "__main__":
    # load it into Chroma
    loaded_db = Chroma(embedding_function=embeddings, persist_directory=persist_dir)
    col_count = loaded_db._collection.count()

    # checks for empty collection. no check for new docs in the directory, just full load
    if col_count == 0:
        print(f"No Collections found.  Loading documents from '{doc_dir}'")
        load_count = doc_to_embeddings(doc_dir)
        col_count = loaded_db._collection.count()
        
    print(f"Count: {col_count}")

    # Show it's working
    query = "visualization"
    docs = loaded_db.similarity_search(query)

    print(f"Results for query: {query}")

    for doc in docs:
        print(f"Metadata: {doc.metadata}")
        print(f"Content Sample: {doc.page_content[:200]}")
