from voice_generator import generate_voice

with open(
    "output/script.txt",
    "r",
    encoding="utf-8"
) as f:
    script = f.read()

generate_voice(
    script,
    "output/voice.mp3"
)

print("\nVoice generated successfully.")