try:
    print("Importing flask...")
    import flask
    print("Importing cv2...")
    import cv2
    print("Importing deepface...")
    from deepface import DeepFace
    print("Importing speech_recognition...")
    import speech_recognition as sr
    print("Importing pyaudio...")
    import pyaudio
    print("Importing librosa...")
    import librosa
    print("All imports successful!")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
