import json

from scene_planner import generate_scene_plan

with open(
    "output/script.txt",
    "r",
    encoding="utf-8"
) as f:

    script = f.read()

scene_plan = generate_scene_plan(script)

print(json.dumps(scene_plan, indent=4))

with open(
    "output/scene_plan.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        scene_plan,
        f,
        indent=4
    )

print("\nScene Plan Saved.")