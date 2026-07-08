from groq import Groq
from config import GROQ_API_KEY
from utils import logger

client = Groq(api_key=GROQ_API_KEY)


def generate_thumbnail_prompts(title, transcript):

    logger.info("Generating thumbnail prompts...")

    prompt = f"""
You are a professional YouTube thumbnail designer.

Create 3 different thumbnail prompts.

Video Title:
{title}

Transcript:
{transcript[:1500]}

Requirements:

- Cinematic
- Bright colors
- High CTR
- Modern YouTube style
- No copyrighted characters

Return exactly like this:

PROMPT 1:
...

PROMPT 2:
...

PROMPT 3:
...
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8
    )

    return response.choices[0].message.content