import json
from pathlib import Path


def load_image_prompts(json_file="output/image_prompts.json"):
    """Load image prompts from JSON file."""

    path = Path(json_file)

    if not path.exists():
        raise FileNotFoundError(f"{json_file} not found.")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_images():
    """
    Placeholder image generation module.
    This currently loads prompts and displays them.
    Later we'll connect it to an AI image service.
    """

    prompts = load_image_prompts()

    print("=" * 60)
    print("IMAGE PROMPTS")
    print("=" * 60)

    for item in prompts:
        print(f"\nScene {item['scene']}")
        print(item["prompt"])


if __name__ == "__main__":
    generate_images()