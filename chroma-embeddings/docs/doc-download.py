
import json

from urllib.parse import urlparse
from langchain_community.document_loaders import UnstructuredURLLoader

input_file = 'input-urls.txt'
url_list = []

def lang_load(urls):
    """ 
    Use LangChain loader to download documents.
    
    Input: urls - a list of URLs to download documents from.
    Output: data - a list of downloaded documents.
    """
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    
    return data


def save_file(url, contents):
    """ 
    Save a file with the modified URL as the name and with doc contents as a JSON object.
    
    Input: 
    url - the URL of the document.
    contents - the contents of the document.
    
    Output: None. A file is saved in the 'raw' directory.
    """
            
    parsed_url = urlparse(url)
    filepath = "raw/" + (parsed_url.netloc + parsed_url.path).replace('/', '_') + ".json"
    
    with open(filepath, 'w') as output_file:
        json.dump({'url': url, 'contents': contents}, output_file)


def load_input_urls(filename):
    """ 
    Load input URLs to download from a TXT file.
    
    Input: filename - the name of the TXT file containing the URLs.
    Output: None. The URLs are added to the global 'url_list'.
    """
    
    with open(filename, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        url_list.append(url)



if __name__ == "__main__":
    load_input_urls(input_file)
    doc_contents = lang_load(url_list)
    
    for doc in doc_contents:
        print(doc.metadata['source'])
        save_file(doc.metadata['source'], doc.page_content)


"""
This script downloads documents from a list of URLs using the LangChain loader.
It then saves each document as a JSON object, with the URL as the name of the file.
"""
