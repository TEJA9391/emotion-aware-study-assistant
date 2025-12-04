import cv2
import numpy as np
from deepface import DeepFace
from datetime import datetime

class EmotionDetector:
    """Emotion detection using DeepFace"""
    
    def __init__(self):
        """Initialize the emotion detector"""
        self.emotions = ['happy', 'sad', 'angry', 'fear', 'surprise', 'neutral', 'disgust']
    
    def analyze_webcam_emotion(self, duration=10):
        """
        Analyze emotion from webcam over a specified duration
        
        Args:
            duration: Duration in seconds to analyze
            
        Returns:
            dict: Dictionary containing emotion analysis results
        """
        try:
            # Open webcam
            cap = cv2.VideoCapture(0)
            
            if not cap.isOpened():
                print("Error: Could not open webcam")
                return None
            
            print(f"Analyzing emotion for {duration} seconds...")
            
            emotions_detected = []
            start_time = datetime.now()
            
            while (datetime.now() - start_time).seconds < duration:
                ret, frame = cap.read()
                
                if not ret:
                    continue
                
                try:
                    # Analyze the frame
                    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                    
                    if isinstance(result, list):
                        result = result[0]
                    
                    emotions_detected.append(result['emotion'])
                    
                except Exception as e:
                    print(f"Error analyzing frame: {e}")
                    continue
            
            # Release the webcam
            cap.release()
            cv2.destroyAllWindows()
            
            if not emotions_detected:
                return None
            
            # Calculate emotion statistics
            emotion_totals = {emotion: 0 for emotion in self.emotions}
            
            for emotion_dict in emotions_detected:
                for emotion, score in emotion_dict.items():
                    if emotion in emotion_totals:
                        emotion_totals[emotion] += score
            
            # Calculate averages
            num_detections = len(emotions_detected)
            emotion_percentages = {
                emotion: (total / num_detections)
                for emotion, total in emotion_totals.items()
            }
            
            # Get dominant emotion
            dominant_emotion = max(emotion_percentages, key=emotion_percentages.get)
            
            return {
                'dominant_emotion': dominant_emotion,
                'emotion_percentages': emotion_percentages,
                'total_detections': num_detections,
                'session_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error in emotion detection: {e}")
            return None
    
    def analyze_image(self, image):
        """
        Analyze emotion from a single image
        
        Args:
            image: Image array (numpy array from cv2 or base64 decoded)
            
        Returns:
            dict: Dictionary containing emotion analysis results
        """
        try:
            # Analyze the image
            result = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
            
            if isinstance(result, list):
                result = result[0]
            
            return {
                'dominant_emotion': result['dominant_emotion'],
                'emotion_percentages': result['emotion'],
                'total_detections': 1,
                'session_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error analyzing image: {e}")
            return None
