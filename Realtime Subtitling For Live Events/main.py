from speech_to_text import listen_and_transcribe
from subtitle_display import display_subtitles

def main():
    print("🎤 LiveSubtitles is starting...")
    for text in listen_and_transcribe():
        display_subtitles(text)

if __name__ == "__main__":
    main()
