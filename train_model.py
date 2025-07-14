import os
import numpy as np
import librosa
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    y, _ = librosa.effects.trim(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    delta = librosa.feature.delta(mfcc)
    delta2 = librosa.feature.delta(mfcc, order=2)
    features = np.concatenate((mfcc, delta, delta2), axis=0)
    return np.mean(features.T, axis=0)

def load_data():
    X, y = [], []
    for label in os.listdir("voices"):
        folder = os.path.join("voices", label)
        if os.path.isdir(folder):
            for file in os.listdir(folder):
                if file.endswith(".wav"):
                    feat = extract_features(os.path.join(folder, file))
                    X.append(feat)
                    y.append(label if label == "hamsini" else "stranger")
    return np.array(X), np.array(y)


X, y = load_data()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


joblib.dump(model, "voice_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("Model and scaler saved.")
