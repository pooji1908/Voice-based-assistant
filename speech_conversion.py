import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")
    except Exception as e:
        print("Say that again......")
        return "None"
    return query
