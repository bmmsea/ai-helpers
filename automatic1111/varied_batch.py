"""
Generate a CSV file for batch image creation that varies in a controlled way.
"""

import csv
import random

# CSV file to use to output prompt batch
out_csv = 'image_batch.csv'

# number of image prompts to generate
total_images = 100

# base character information
character_prompts = [
    "alice in wonderland",
    "alice, through the looking glass"
]
# adjectives to describe the character
adj_prompts = [
    "heroic",
    "fierce",
    "curious"
]
# information about the scene or setting
scene_prompts = [
    "in armor, holding sword, fighting a dragon",
    "lost in the woods",
    "tea party with mad hatter",
    "captured by the queen of hearts",
    "meeting the cheshire cat"
]
# include this in every prompt
always_prompt = 'highly detailed, 4k, colorful, fantasy style'

# rotate the negative to vary output, with consistent themes
negative_prompts = [
    "unattractive, deformed", 
    "dirty, misshapen"
]
# add to every negative prompt
always_negative = 'nsfw'

# set of step values. single value works
steps = [20, 25, 30]

with open(out_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["prompt", "negative_prompt", "width", "height", "steps", "seed", "restore_faces", "face_restoration"])
    
    for _ in range(total_images):
        # leaving any blank will result in extra commas
        prompt = f"{random.choice(character_prompts)}, {random.choice(adj_prompts)}, {random.choice(scene_prompts)}, {always_prompt}"
        negative_prompt = f"{random.choice(negative_prompts)}, {always_negative}"
        
        step_count = random.choice(steps)
        
        # image size can be changed here
        writer.writerow([prompt, negative_prompt, 512, 768, step_count, -1, True, "GFPGAN"])
        
