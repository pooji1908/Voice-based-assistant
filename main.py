from text_generation import get_reply
from speech_conversion import take_command, speak
from dotenv import load_dotenv
import os
import webbrowser

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def main():
    while True:
        query = take_command().lower()
        if query == "none":
            continue

        ans = get_reply(query, api_key)
        
        print(ans)
        speak(ans)
        if "open youtube" in query:
            webbrowser.open('https://www.youtube.com')
        elif "open google" in query:
            webbrowser.open('https://www.google.com')
        elif 'bye' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
