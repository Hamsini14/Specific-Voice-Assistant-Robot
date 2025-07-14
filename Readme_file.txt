===============================================
VOICE-CONTROLLED PERSONAL ASSISTANT ROBOT
(Specific Speaker Recognition + Command Control)
===============================================

📌 PROJECT DESCRIPTION:
This project implements a smart voice-controlled robot that responds only to a specific user's voice. It authenticates the speaker using machine learning (MFCC + RandomForest), ensuring secure command control for robot movements and basic assistant features like telling time and weather.

👤 Developer: Hamsini,Deekshith,Deepshika and Chinmayi

📂 FOLDER STRUCTURE:
- voices/                  → Folder storing voice samples
  └── hamsini/  
  └── stranger/           → Contains labeled .wav voice recordings
- test.wav                 → Temporary file for voice verification and command
- voice_model.pkl          → Trained voice recognition model
- scaler.pkl               → Feature scaler for prediction

🧠 TECHNOLOGIES USED:
- Python (Librosa, SoundDevice, SpeechRecognition, Pyttsx3)
- Machine Learning (MFCC + Random Forest)
- Arduino + Serial Communication
- OpenWeatherMap API (for weather info)

🔧 HARDWARE REQUIRED:
- Arduino Uno or ESP32
- Motor driver & DC motors (L298N)
- Chassis with wheels
- USB cable and jumper wires
- Laptop with microphone

📦 PYTHON MODULES TO INSTALL:
pip install sounddevice
pip install scipy
pip install numpy
pip install librosa
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install joblib

🛠 HOW TO RUN:

1. Record Training Samples:
----------------------------
Run the script to record new samples:
> python record_samples.py

2. Train the Model:
-------------------
> python train_model.py

3. Run the Main Assistant:
--------------------------
> python main.py

This will:
- Ask the user to speak.
- Verify the speaker.
- If verified, execute robot movement or assistant commands (e.g., "forward", "weather").

4. Upload Arduino Code:
-----------------------
Upload `voice_robot.ino` to Arduino via Arduino IDE. It listens for serial commands: 'F', 'B', 'L', 'R', 'S'.

💡 VOICE COMMANDS SUPPORTED:
- "forward"
- "backward"
- "left"
- "right"
- "stop"
- "what is the time"
- "what is the weather"

🔐 SECURITY:
Only the trained voice (e.g., "hamsini") can control the robot. All other voices are rejected with "Unauthorized voice detected."

🌐 WEATHER API:
Uses OpenWeatherMap API to fetch real-time weather:
Update your `API_KEY` in the script.

🧠 NOTE:
Ensure microphone access is enabled.
Robot will not respond if voice verification fails.

