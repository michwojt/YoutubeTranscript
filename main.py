# youtube_transcriber.py

import os
import sys
import re
import whisper
import subprocess
from datetime import datetime

def download_video(url):
    print("[+] Downloading full video from YouTube...")

    video_file = "video.mp4"

    # Get video title
    command_info = [
        "yt-dlp",
        "--skip-download",
        "--print", "%(title)s",
        url
    ]
    result = subprocess.run(command_info, stdout=subprocess.PIPE, text=True, check=True)
    title = result.stdout.strip()

    # Download best video+audio in mp4 format
    command_download = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4][height<=720]+bestaudio[ext=m4a]/best[ext=mp4][height<=720]",
        "-o", video_file,
        url
    ]
    subprocess.run(command_download, check=True)

    return title, video_file

def clean_title(title):
    # Remove unsafe filename characters and spaces
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace(" ", "_")
    return title

def transcribe_audio(file_path):
    print("[+] Transcribing audio with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result

def save_transcript(result, title, filename=None):
    if filename is None:
        today = datetime.today().strftime('%Y-%m-%d')
        safe_title = clean_title(title)
        filename = f"transcript_{today}_{safe_title}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()

            # Format timestamps
            start_min = int(start // 60)
            start_sec = int(start % 60)
            end_min = int(end // 60)
            end_sec = int(end % 60)

            timestamp = f"[{start_min:02d}:{start_sec:02d} --> {end_min:02d}:{end_sec:02d}]"
            f.write(f"{timestamp} {text}\n")
    print(f"[+] Transcript with timestamps saved to {filename}")

def main():
    # if len(sys.argv) != 2:
    #     print("Usage: python youtube_transcriber.py <YouTube_URL>")
    #     sys.exit(1)

    # url = sys.argv[1]
    url = "https://www.youtube.com/watch?v=mMaTteE19rA"  # << your video

    try:
        title, video_file = download_video(url)
        transcript_result = transcribe_audio(video_file)
        save_transcript(transcript_result, title)
    except subprocess.CalledProcessError as e:
        print("Error during downloading or converting video:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
