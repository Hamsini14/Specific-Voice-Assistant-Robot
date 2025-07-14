import sounddevice as sd
import numpy as np
import joblib
import librosa
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import serial
import time
import datetime
import requests

API_KEY = "764cc991ef07e5fb213a35f5ec1f6ae3"
CITY = "Bangalore"


ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

model = joblib.load("voice_model.pkl")
scaler = joblib.load("scaler.pkl")

import sounddevice as sd
import soundfile as sf

engine=pyttsx3.init()
engine.setProperty('rate',150)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def record_voice(filename="test.wav", duration=4, fs=16000):
    speak("Speak now")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, audio, fs, subtype='PCM_16')
    print("Voice recorded.")

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            weather_info = f"The weather in {CITY} is {desc} with a temperature of {temp:.1f}°C"
            speak(weather_info)
        else:
            speak("Sorry, I couldn't fetch the weather right now.")
    except Exception as e:
        speak("An error occurred while fetching weather.")


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    y, _ = librosa.effects.trim(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    delta = librosa.feature.delta(mfcc)
    delta2 = librosa.feature.delta(mfcc, order=2)
    features = np.concatenate((mfcc, delta, delta2), axis=0)
    return np.mean(features.T, axis=0)

def verify_user():
    record_voice()
    feat = extract_features("test.wav")
    feat_scaled = scaler.transform([feat])
    prediction = model.predict(feat_scaled)[0]
    print(f" Predicted: {prediction}")
    return prediction == "hamsini"

import speech_recognition as sr

def recognize_command():
    recognizer = sr.Recognizer()
    with sr.AudioFile("test.wav") as source:
        audio = recognizer.record(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand.")
        return ""
    except sr.RequestError as e:
        print(f" API error: {e}")
        return ""

def act_on_command(cmd):
    if "time" in cmd:
        now = datetime.datetime.now().strftime("%I:%M %p")  # e.g., 10:42 AM
        speak(f"The current time is {now}")
    elif "weather" in cmd:
        get_weather()
    elif "forward" in cmd:
        ser.write(b'F')
        speak("Moving forward")
    elif "backward" in cmd:
        ser.write(b'B')
        speak("Moving backward")
    elif "left" in cmd:
        ser.write(b'L')
        speak("Turning left")
    elif "right" in cmd:
        ser.write(b'R')
        speak("Turning right")
    elif "stop" in cmd:
        ser.write(b'S')
        speak("Stopping")
    else:
        speak("Unknown command")



speak("Voice authentication ready.")
while True:

    speak("\nPlease verify your voice to control the robot.")
    if verify_user():
        cmd = recognize_command()
        act_on_command(cmd)
    else:

        speak("Unauthorized voice detected.")