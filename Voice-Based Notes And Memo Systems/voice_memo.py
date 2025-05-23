import speech_recognition as sr
import pyttsx3
from tkinter import *
import os
import datetime

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_note():
    try:
        with sr.Microphone() as source:
            speak("Listening for your note.")
            audio = recognizer.listen(source)
            note = recognizer.recognize_google(audio)
            note_text.insert(END, f"{note}\n")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
    except sr.RequestError:
        speak("Speech recognition service error.")

def save_note():
    note_content = note_text.get("1.0", END).strip()
    if note_content:
        filename = f"notes/note_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(note_content)
        speak("Note saved successfully.")
        note_text.delete("1.0", END)

root = Tk()
root.title("Voice Memo System")

note_text = Text(root, height=15, width=50)
note_text.pack()

Button(root, text="Start Recording", command=record_note).pack()
Button(root, text="Save Note", command=save_note).pack()

os.makedirs("notes", exist_ok=True)
root.mainloop()
