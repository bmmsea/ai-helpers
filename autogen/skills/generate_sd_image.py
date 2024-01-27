
##### Begin of generate_sd_images #####

"""
Generate an image locally when running automatic1111 
API Docs:  https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API

The API is not enabled by default in Automatic1111, and must be enabled in the command line arguments
  in webui-user.sh -> export COMMANDLINE_ARGS="--api"
"""
from pathlib import Path
from PIL import Image
from typing import List

import json
import requests
import io
import base64

# Format: protocol://server:port
base_url = "http://127.0.0.1:7860"

    
def generate_sd_images(query: str, image_size: str = "1024x1024") -> List[str]:
    """
    Function to paint, draw or illustrate images based on the users query or request. Generates images locally with the automatic1111 API and saves them to disk.  Use the code below anytime there is a request to create an image.

    :param query: A natural language description of the image to be generated.
    :param image_size: The size of the image to be generated. (default is "1024x1024")
    :return: A list of filenames for the saved images.
    """
    # Split the image size string at "x"
    #   Keeping the input format consistent with the default generate_and_save_images
    parts = image_size.split("x")
    image_width = parts[0]
    image_height = parts[1]

    # list of file paths returned to AutoGen
    saved_files = []

    payload = {
        "prompt": query,
        "steps": 20,
        "width": image_width,
        "height": image_height
    }

    api_url = f"{base_url}/sdapi/v1/txt2img"
    response = requests.post(url=api_url, json=payload)

    if response.status_code == 200:
        r = response.json()

        info_json = json.loads(r['info'])
        seed = info_json['seed']

        # using the seed in the file name to allow for multiple images
        file_name = f"{seed}_output.png"
        file_path = Path(file_name)

        with Image.open(io.BytesIO(base64.b64decode(r['images'][0]))) as image:
            image.save(file_path)
            print(f"Image saved to {file_path}")
            
            saved_files.append(str(file_path))
    else:
        print(f"Failed to download the image from {api_url}")
        
    return saved_files

# Example usage of the function:
#img_list = generate_sd_images("cute cudddly baby sloth, cgi cartoon, big eyes, highly detailed fur", "512x512")
#print(img_list)

#### End of generate_sd_images ####
