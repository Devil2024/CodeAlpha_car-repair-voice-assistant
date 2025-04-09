import speech_recognition as sr
import pyttsx3
import requests
import time

# Initialize TTS engine
engine = pyttsx3.init()

# Initialize recognizer with noise calibration
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000  # Adjust based on mic sensitivity
recognizer.pause_threshold = 1.5  # Pause duration to end listening

def speak(response):
    segments = response.split('\n\n')  # Splitting by paragraphs
    for segment in segments:
        engine.say(segment)
        engine.runAndWait()
    time.sleep(0.5)  # Pause after speaking

def listen():
    with sr.Microphone() as source:
        print("Calibrating mic for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio).lower()
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return None
        except Exception as e:
            print(f"Audio error: {str(e)}")
            return None

def get_rasa_response(text):
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": text},
            timeout=5
        )
        # Extract all messages from the response
        messages = response.json()
        # Combine the text from all messages into one full response
        full_text = " ".join([msg.get("text", "") for msg in messages])
        return full_text
    except Exception as e:
        print(f"Rasa error: {str(e)}")
        return "I'm having trouble connecting to the service."

# Main conversation loop
if __name__ == "__main__":
    speak("Hello! How can I assist you with your car today?")
    
    while True:
        user_input = listen()
        if not user_input:
            speak("Sorry, I didn't catch that. Could you repeat?")
            continue
            
        print(f"You: {user_input}")
        response = get_rasa_response(user_input)
        print(f"Assistant: {response}")
        speak(response)
        
        # Exit condition (optional)
        if "exit" in user_input or "goodbye" in user_input:
            speak("Goodbye! Have a great day.")
            break