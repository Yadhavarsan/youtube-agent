from pathlib import Path
import whisper

from config import WHISPER_MODEL, OUTPUT_DIR
from utils import logger


def transcribe(video_path):
    """
    Transcribe a video file using Whisper.
    """

    video_path = Path(video_path)

    if not video_path.exists():
        raise FileNotFoundError(f"{video_path} not found")

    logger.info(f"Loading Whisper model: {WHISPER_MODEL}")

    model = whisper.load_model(WHISPER_MODEL)

    logger.info("Starting transcription...")

    result = model.transcribe(str(video_path))

    transcript = result["text"]

    transcript_file = OUTPUT_DIR / "transcript.txt"

    transcript_file.write_text(transcript, encoding="utf-8")

    logger.info(f"Transcript saved to {transcript_file}")

    return transcript