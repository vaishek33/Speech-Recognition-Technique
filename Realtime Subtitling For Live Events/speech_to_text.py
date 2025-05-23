import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎙️ Listening...")

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                yield text
            except sr.UnknownValueError:
                yield "[Unrecognized speech]"
            except Exception as e:
                yield f"[Error: {e}]"
