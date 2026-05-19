import speech_recognition as sr

DISTRESS_WORDS = [
    "help",
    "save me",
    "bachao",
    "emergency",
    "danger"
]

def detect_distress():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("Detected:", text)

        for word in DISTRESS_WORDS:
            if word in text:
                return {
                    "distress": True,
                    "text": text
                }

        return {
            "distress": False,
            "text": text
        }

    except Exception as e:
        return {
            "distress": False,
            "error": str(e)
        }