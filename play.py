import sounddevice as sd
import scipy.io.wavfile as wav


file_path = "voices/stranger/186.wav"


fs, data = wav.read(file_path)
print(f"Playing: {file_path}")
sd.play(data, fs)
sd.wait()
print("Done")
