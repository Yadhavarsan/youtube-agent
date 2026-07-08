import json

from image_prompt_generator import generate_image_prompts

with open(
    "output/scene_plan.json",
    "r",
    encoding="utf-8"
) as f:
    scenes = json.load(f)

prompts = generate_image_prompts(scenes)

print(json.dumps(prompts, indent=4))

with open(
    "output/image_prompts.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(prompts, f, indent=4)

print("\nImage prompts saved.")