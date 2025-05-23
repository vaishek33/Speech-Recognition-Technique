import speech_recognition as sr
import pyttsx3
from tkinter import *
from tkinter import messagebox
import os
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Create notes directory if not exists
os.makedirs("notes", exist_ok=True)

def speak(text):
    """Speak out the provided text."""
    engine.say(text)
    engine.runAndWait()

def record_note():
    """Record voice and convert to text."""
    try:
        with sr.Microphone() as source:
            speak("Listening... Please speak your note.")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            note = recognizer.recognize_google(audio)
            note_text.insert(END, f"{note}\n")
            speak("Note recorded.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your voice.")
    except sr.RequestError:
        speak("Could not request results from Google.")
    except sr.WaitTimeoutError:
        speak("No speech detected. Please try again.")

def save_note():
    """Save the text in the note_text widget to a file."""
    content = note_text.get("1.0", END).strip()
    if not content:
        speak("Note is empty. Nothing to save.")
        return
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"notes/note_{timestamp}.txt"
    with open(filename, "w") as file:
        file.write(content)
    note_text.delete("1.0", END)
    speak("Note saved successfully.")

def read_notes():
    """Read all saved notes aloud."""
    files = os.listdir("notes")
    if not files:
        speak("No notes available.")
        return
    speak("Reading your saved notes.")
    for fname in sorted(files):
        with open(os.path.join("notes", fname), "r") as file:
            content = file.read()
            speak(f"Note from {fname}: {content}")

# GUI setup
root = Tk()
root.title("Voice-Based Notes and Memo System")
root.geometry("500x400")

note_text = Text(root, wrap=WORD, font=("Arial", 12))
note_text.pack(pady=10, padx=10, expand=True, fill=BOTH)

frame = Frame(root)
frame.pack(pady=10)

Button(frame, text="🎙️ Record Note", command=record_note, width=20).pack(side=LEFT, padx=5)
Button(frame, text="💾 Save Note", command=save_note, width=20).pack(side=LEFT, padx=5)
Button(frame, text="📖 Read Notes", command=read_notes, width=20).pack(side=LEFT, padx=5)

root.mainloop()
