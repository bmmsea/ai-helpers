"""
Generate an image batch from a CSV file with automatic1111
API Docs:  https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API

The API is not enabled by default in Automatic1111, and must be enabled in the command line arguments
  in webui-user.sh -> export COMMANDLINE_ARGS="--api"

CSV file headers will be used as keys, and row contents for values in the JSON payload to the /sdapi/v2/txt2img API
  * For a random seed, use -1
  * Absence of a column in the CSV file will omit it from the payload and use the server's last values
  * Blank values will result in a failed request with a 422 response code
"""

from pathlib import Path
from PIL import Image
from typing import List

import base64
import csv
import io
import json
import requests


# Base URL Format: protocol://server:port
base_url = "http://127.0.0.1:7860"
csv_file = 'image_batch.csv'

# edit to use a path other than the script execution directory
save_path = "/tmp"
#save_path = None


def generate_sd_images(**kwargs):
    """
    Function to paint, draw or illustrate a single image. Generates images locally with the automatic1111 API and save them to disk.  
    
    parameter: **kwargs key/value pairs to send as the payload to the API, column headers from the CSV file as keys, row contents for values
    """

    for key, value in kwargs.items():
        if value.isdigit():  # Check if the value is a digit
            kwargs[key] = int(value)  # Convert to integer for proper payload format

    api_url = f"{base_url}/sdapi/v1/txt2img"
    response = requests.post(url=api_url, json=kwargs)

    if response.status_code == 200:
        r = response.json()
        
        # r['info'] contains what the server used to generate the image, in addition to the payload
        #print(f"Response Info JSON: {r['info']}")
        
        info_json = json.loads(r['info'])
        seed = info_json['seed']
        job_timestamp = info_json['job_timestamp']
        
        print(f"Timestamp: {job_timestamp}")

        # using the job_timestamp and seed for unique file names
        file_name = f"{job_timestamp}_{seed}_output.png"
        
        if save_path:
            file_path = f"{save_path}/{file_name}"
        else:
            file_path = Path(file_name)
        

        with Image.open(io.BytesIO(base64.b64decode(r['images'][0]))) as image:
            image.save(file_path)
            print(f"Image saved to {file_path}\n")

    else:
        print(f"Failed to download the image from {api_url}")
        print(f"Response: {response.status_code}")
        print(f"{response.content}\n")
        


if __name__ == "__main__": 
    # Open the CSV file
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Note: random seeds can be used by using the value of -1
        for row in csv_reader:
            # Call the function with the extracted values in as a Dict
            print(f"Prompt: {row['prompt']}\tSize: {row['width']} x {row['height']}")
            generate_sd_images(**row)
            

            
