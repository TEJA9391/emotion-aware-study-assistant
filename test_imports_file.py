import sys
import traceback

with open('import_log.txt', 'w') as f:
    try:
        f.write("Starting imports...\n")
        import flask
        f.write("Imported flask\n")
        import cv2
        f.write("Imported cv2\n")
        from deepface import DeepFace
        f.write("Imported deepface\n")
        import speech_recognition as sr
        f.write("Imported speech_recognition\n")
        import pyaudio
        f.write("Imported pyaudio\n")
        import librosa
        f.write("Imported librosa\n")
        f.write("All imports successful!\n")
    except Exception as e:
        f.write(f"Import failed: {e}\n")
        traceback.print_exc(file=f)
