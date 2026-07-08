from pathlib import Path

from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
)


def create_video(
    images_folder,
    audio_file,
    output_file,
):
    """
    Create a slideshow video using images and narration audio.
    """

    images = sorted(Path(images_folder).glob("*.*"))

    if not images:
        raise Exception("No images found inside output/images")

    audio = AudioFileClip(audio_file)

    duration_per_image = audio.duration / len(images)

    clips = []

    for image in images:

        clip = (
            ImageClip(str(image))
            .with_duration(duration_per_image)
        )

        clips.append(clip)

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    final_video = final_video.with_audio(audio)

    final_video.write_videofile(
        output_file,
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )