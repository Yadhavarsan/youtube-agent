import json
from groq import Groq

from config import GROQ_API_KEY
from utils import logger

client = Groq(api_key=GROQ_API_KEY)


def generate_scene_plan(script):

    logger.info("Generating Scene Plan...")

    prompt = f"""
You are an expert storyboard artist.

Convert this YouTube script into scenes.

Script:

{script}

Return ONLY JSON.

Example:

[
{{
"scene":1,
"duration":"0-10 sec",
"visual":"...",
"camera":"...",
"voice":"..."
}}
]
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.6,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return json.loads(response.choices[0].message.content)