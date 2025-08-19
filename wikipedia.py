import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia


engine = pyttsx3.init()
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

try:
    query = recognizer.recognize_google(audio)
    summary = wikipedia.summary(query, sentences=4)
    print(summary)
    engine.say(summary)
    engine.runAndWait()
except:
    engine.say("Sorry, I could not find information.")
    engine.runAndWait()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 1000
    recognizer.dynamic_energy_threshold = False

    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query.lower()
        except:
            return None

def chatbot_response(query):
    
    if "hello" in query:
        return "Hello! How can I help you?"
    
    elif "your name" in query:
        return "I am your assistant."
    
    elif "open browser" in query or "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening browser."
    
    elif "open youtube" in query or "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "Opening youtube."
    
    elif "open instagram" in query or "open instagram" in query:
        webbrowser.open("https://www.instagram.com")
        return "Opening instagram."
    
    elif "open twitter" in query or "open twitter" in query:
        webbrowser.open("")
        return "Opening twitter."
    
    elif "bye" in query or "exit" in query or "stop" in query:
        return "Goodbye!"
    else:
        return "I didn't understand that."

if __name__ == "__main__":
    speak("Hello. boyzz !! How are you!!")

    while True:
        query = listen()
        if query:
            response = chatbot_response(query)
            speak(response)
            if "bye" in query or "exit" in query or "stop" in query:
                break
