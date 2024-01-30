import csv
import random

prompts = ["pic of a sexy female model", "pic of a beautiful landscape", "pic of a futuristic city", "pic of a medieval castle", "pic of a cute puppy"]
negative_prompts = ["unattractive, fat, deformed, bad hands, asian", "dull, boring, flat, monochrome", "old, ruined, dirty, polluted", "modern, small, simple, bright", "ugly, scary, big, dirty"]

with open('image_generation_prompts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["prompt", "negative_prompt", "width", "height", "steps", "seed", "restore_faces", "face_restoration"])
    
    for _ in range(100):
        prompt = random.choice(prompts)
        negative_prompt = random.choice(negative_prompts)
        writer.writerow([prompt, negative_prompt, 512, 768, 25, -1, True, "GFPGAN"])
