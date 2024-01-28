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
save_dir = '/tmp'
image_width = 512
image_height = 768

payload = {
    "prompt": "cute cudddly baby sloth, cgi cartoon, pixar style, big eyes, highly detailed fur",
    "steps": 20,
    "width": image_width,
    "height": image_height
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

info_json = json.loads(r['info'])
seed = info_json['seed']
print(f"Seed: {seed}")

# change the filename to whatever you want to use
file_path = f"{save_dir}/{seed}_output.png"

image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
image.save(file_path)

