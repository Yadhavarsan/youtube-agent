import asyncio
import edge_tts
from utils import logger


async def text_to_speech(text, output_file, voice="en-US-AndrewNeural"):
    """
    Convert text into speech using Microsoft Edge TTS.

    Args:
        text (str): Text to convert.
        output_file (str): Output MP3 filename.
        voice (str): Edge TTS voice.
    """

    logger.info("Generating voice...")

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="+0%",
        pitch="+0Hz"
    )

    await communicate.save(output_file)

    logger.info(f"Voice saved to {output_file}")


def generate_voice(text, output_file):
    """
    Synchronous wrapper.
    """
    asyncio.run(text_to_speech(text, output_file))