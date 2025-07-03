
A simple Python script that downloads a YouTube video, transcribes its audio using OpenAI's Whisper model, and saves the transcript with timestamps.

---

## 🔧 Features

- Downloads YouTube videos at 720p resolution using `yt-dlp`
- Transcribes audio locally using [Whisper](https://github.com/openai/whisper)
- Outputs a clean `.txt` transcript file with timestamps
- Auto-generates safe filenames based on the video title and date

---

## 🧰 Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/)
- [openai/whisper](https://github.com/openai/whisper)
- PyTorch (required for Whisper)

** Usage**

By default, the script uses a hardcoded test video link. To use your own, uncomment the lines with sys.argv in main().

The transcript will be saved to a file named:

transcript_YYYY-MM-DD_<video_title>.txt

Example contents:

[00:00 --> 00:10] Welcome to the channel. Today we’re discussing...
[00:10 --> 00:22] In this part, we’ll look at the first example...

 Example Workflow

    Downloads the video as video.mp4

    Transcribes the audio

    Saves to a readable transcript with timestamps
