from flask import Flask, render_template, request, jsonify, session
import cv2
import numpy as np
from fer import FER
import base64
from datetime import datetime
import json
import os
from study_recommendations import get_study_recommendations, get_motivational_quote
from voice_analyzer import analyze_voice_emotion

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Initialize emotion detector
emotion_detector = FER(mtcnn=True)

# Ensure data directory exists
os.makedirs('data/user_sessions', exist_ok=True)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard page"""
    return render_template('dashboard.html')

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    """Analyze emotion from webcam image"""
    try:
        data = request.json
        image_data = data.get('image')
        
        if not image_data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Decode base64 image
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        
        # Convert to numpy array
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({'error': 'Failed to decode image'}), 400
        
        # Detect emotions
        emotions = emotion_detector.detect_emotions(img)
        
        if not emotions:
            return jsonify({
                'success': False,
                'message': 'No face detected. Please ensure your face is visible.'
            })
        
        # Get dominant emotion
        dominant_emotion = max(emotions[0]['emotions'].items(), key=lambda x: x[1])
        emotion_name = dominant_emotion[0]
        confidence = dominant_emotion[1]
        
        # Get study recommendations
        recommendations = get_study_recommendations(emotion_name)
        quote = get_motivational_quote(emotion_name)
        
        # Save to session
        if 'emotion_history' not in session:
            session['emotion_history'] = []
        
        session['emotion_history'].append({
            'emotion': emotion_name,
            'confidence': float(confidence),
            'timestamp': datetime.now().isoformat()
        })
        session.modified = True
        
        return jsonify({
            'success': True,
            'emotion': emotion_name,
            'confidence': float(confidence),
            'all_emotions': emotions[0]['emotions'],
            'recommendations': recommendations,
            'quote': quote
        })
        
    except Exception as e:
        print(f"Error in analyze_emotion: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_voice', methods=['POST'])
def analyze_voice():
    """Analyze voice emotion from audio"""
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        # Save temporarily
        temp_path = 'data/temp_audio.wav'
        audio_file.save(temp_path)
        
        # Analyze voice emotion
        result = analyze_voice_emotion(temp_path)
        
        # Clean up
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        return jsonify({
            'success': True,
            'emotion': result.get('emotion', 'neutral'),
            'text': result.get('text', ''),
            'confidence': result.get('confidence', 0.0)
        })
        
    except Exception as e:
        print(f"Error in analyze_voice: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_session_data')
def get_session_data():
    """Get session emotion history"""
    emotion_history = session.get('emotion_history', [])
    return jsonify({
        'success': True,
        'history': emotion_history
    })

@app.route('/clear_session', methods=['POST'])
def clear_session():
    """Clear session data"""
    session.clear()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
