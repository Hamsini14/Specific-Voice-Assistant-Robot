import os
import sounddevice as sd
from scipy.io.wavfile import write

user_name = "hamsini"
sample_rate = 44100
duration = 5
num_new_samples = 10

output_dir = f"voices/{user_name}"
os.makedirs(output_dir, exist_ok=True)


start_index = 191

print(f"\nRecording {num_new_samples} new voice samples for {user_name} starting from {start_index}\n")

for i in range(num_new_samples):
    current_index = start_index + i
    print(f"Recording sample {current_index} - Speak now!")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()

    file_path = os.path.join(output_dir, f"{current_index}.wav")
    write(file_path, sample_rate, audio)
    print(f"Saved: {file_path}\n")

print(f" Done! New voice samples saved to: {output_dir}")
