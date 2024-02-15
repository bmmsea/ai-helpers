
from urllib.parse import urlparse
from langchain_community.document_loaders import UnstructuredURLLoader

input_file = 'input-urls.txt'
urls = []

def lang_load():
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

def save_file(filepath, contents):
    with open(filename, 'wb') as output_file:
        output_file.write(response.content)

def load_input_urls(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        urls.append(url)
        
        parsed_url = urlparse(url)
        filename = "docs/raw/" + (parsed_url.netloc + parsed_url.path).replace('/', '_')
        
        print(filename)
        



if __name__ == "__main__":
    load_input_urls(input_file)
