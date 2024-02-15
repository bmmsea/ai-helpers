import os
import requests
from urllib.parse import urlparse

def download_documents():
    with open('input-urls.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        response = requests.get(url)
        parsed_url = urlparse(url)
        filename = "docs/raw/" + (parsed_url.netloc + parsed_url.path).replace('/', '_')

        with open(filename, 'wb') as output_file:
            output_file.write(response.content)

if __name__ == "__main__":
    download_documents()
