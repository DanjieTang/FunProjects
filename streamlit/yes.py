import streamlit as st
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment

# Function to record audio
def record_audio(duration=5, fs=44100):
    st.write("Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    st.write("Recording stopped")
    return myrecording, fs

# Function to save recording as WAV
def save_as_wav(recording, fs, filename='output.wav'):
    write(filename, fs, recording)  # Save as WAV file
    st.write(f"File saved as {filename}")

# Streamlit interface
st.title("Audio Recorder")
if st.button("Record Audio"):
    duration = 5  # Duration in seconds
    recording, fs = record_audio(duration=duration)
    save_as_wav(recording, fs)