import speech_recognition as sr
import pyautogui
import json
from utils.command_mapper import execute_command

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)

def recognize_voice_command(recognizer, mic):
    with mic as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("API unavailable.")
    return None

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    config = load_config()

    with mic:
        recognizer.adjust_for_ambient_noise(mic)

    while True:
        command = recognize_voice_command(recognizer, mic)
        if command:
            execute_command(command, config)

if __name__ == "__main__":
    main()
