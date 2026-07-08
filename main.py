from pathlib import Path
import json

from transcriber import transcribe
from metadata import generate_metadata
from thumbnail import generate_thumbnail_prompts

VIDEO = Path("input/sample.mp4")

print("=" * 60)
print("YOUTUBE AI AGENT")
print("=" * 60)

print("\nSTEP 1 : Transcribing...\n")
transcript = transcribe(VIDEO)

print("Done\n")

print("STEP 2 : Metadata...\n")
metadata = generate_metadata(transcript)

with open("output/metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=4)

print("Done\n")

print("STEP 3 : Thumbnail Prompts...\n")

thumbnail = generate_thumbnail_prompts(
    metadata["title"],
    transcript
)

with open(
    "output/thumbnail_prompts.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(thumbnail)

print(thumbnail)

print("\nEverything completed successfully.")