from script_writer import generate_script

topic = "How AI is changing YouTube Automation"

script = generate_script(topic)

print(script)

with open(
    "output/script.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(script)

print("\nScript Saved.")