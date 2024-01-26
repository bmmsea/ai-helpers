"""
Generate an image locally when running automatic1111 
API Docs:  https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API

The API is not enabled by default, and must be enabled in the command line arguments

"""

import json
import requests
import io
import base64
from PIL import Image

url = "http://127.0.0.1:7860"

payload = {
    "prompt": "juggernaut from xmen",
    "steps": 20
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
image.save('output.png')

