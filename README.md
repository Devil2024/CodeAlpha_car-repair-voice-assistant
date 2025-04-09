# CodeAlpha_car-repair-voice-assistant
This project is a car repair voice assistant that uses Rasa for chatbot interaction and integrates speech recognition and text-to-speech functionalities. The assistant is designed to help users diagnose car issues and provide repair suggestions based on natural language input.

Features
Voice Recognition: The assistant listens to user input via a microphone and converts it to text.

Rasa Integration: Utilizes the Rasa framework to process the user input and generate a relevant response.

Text-to-Speech: The assistant speaks out the responses to the user.

Local Setup: This application runs locally, meaning no external servers are required to interact with the assistant.

Customizable Responses: You can modify the Rasa chatbot and responses based on your specific car repair database.

Prerequisites
Before you run this project, make sure you have the following installed:

Python 3.x

Rasa installed locally and running (Rasa server must be up)

Libraries:

speech_recognition

pyttsx3

requests

How It Works
Speech Recognition: The assistant listens for the user's input using the speech_recognition library. It processes audio from the microphone and converts it into text.

Rasa Chatbot: The user’s text input is sent to the locally running Rasa server, which processes the input and generates a response based on pre-defined stories and intents related to car repair.

Text-to-Speech: The assistant speaks the response using the pyttsx3 library.

Exit Condition
You can stop the conversation by saying "exit" or "goodbye".
