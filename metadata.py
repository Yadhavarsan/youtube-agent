import json
from groq import Groq

from config import GROQ_API_KEY
from utils import logger

client = Groq(api_key=GROQ_API_KEY)


def generate_metadata(transcript):

    prompt = f"""
You are an expert YouTube SEO strategist.

Analyze the transcript below and generate metadata.

Transcript:
{transcript}

Return ONLY valid JSON.

Example:

{{
"title":"Example Title",
"description":"Example description",
"tags":["AI","Python","Automation"],
"category":"Education"
}}
"""

    logger.info("Generating metadata...")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return json.loads(response.choices[0].message.content)