from groq import Groq
from config import GROQ_API_KEY
from utils import logger

client = Groq(api_key=GROQ_API_KEY)


def generate_script(topic):

    logger.info("Generating YouTube script...")

    prompt = f"""
You are an expert YouTube script writer.

Write a complete YouTube script.

Topic:

{topic}

Requirements

- Catchy Hook
- Strong Introduction
- 5 Main Sections
- Conclusion
- Call To Action

Length:

1200-1800 words.

Return only the script.
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