from pathlib import Path
import json

from transcriber import transcribe
from metadata import generate_metadata

VIDEO = Path("input/sample.mp4")

print("="*60)
print("YOUTUBE AI AGENT")
print("="*60)

print("\nSTEP 1 : Transcribing Video...\n")

transcript = transcribe(VIDEO)

print("Transcript Complete\n")

print("STEP 2 : Generating Metadata...\n")

metadata = generate_metadata(transcript)

print(json.dumps(metadata, indent=4))

with open(
    "output/metadata.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        metadata,
        f,
        indent=4
    )

print("\nMetadata Saved Successfully.")