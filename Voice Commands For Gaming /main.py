import speech_recognition as sr
import pyautogui
import json
from utils.command_mapper import execute_command

def load_config(config_path="config.json"):
    """
    Load the command configuration from a JSON file.
    """
    try:
        with open(config_path, "r") as file:
            config = json.load(file)
        print("[INFO] Configuration loaded.")
        return config
    except FileNotFoundError:
        print("[ERROR] Config file not found.")
        return {}
    except json.JSONDecodeError:
        print("[ERROR] Failed to parse config file.")
        return {}

def recognize_voice_command(recognizer, microphone):
    """
    Capture voice from the microphone and convert it to text using Google Speech Recognition.
    """
    with microphone as source:
        print("[INFO] Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"[INFO] Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        print("[WARNING] Could not understand audio.")
    except sr.RequestError:
        print("[ERROR] Could not request results from speech recognition service.")
    return None

def main():
    """
    Main loop: loads config, initializes microphone and recognizer, and processes voice commands.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    config = load_config()

    if not config:
        print("[ERROR] Exiting due to missing configuration.")
        return

    with microphone:
        recognizer.adjust_for_ambient_noise(microphone)

    print("[INFO] Voice command system is active. Say a command...")

    try:
        while True:
            voice_command = recognize_voice_command(recognizer, microphone)
            if voice_command:
                execute_command(voice_command, config)
    except KeyboardInterrupt:
        print("\n[INFO] Voice command system terminated by user.")

if __name__ == "__main__":
    main()
