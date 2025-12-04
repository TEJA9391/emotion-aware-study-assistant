import random
from datetime import datetime

class StudyRecommendations:
    def __init__(self):
        self.recommendations = {
            'happy': {
                'study_tips': [
                    "Great mood for learning! Try tackling challenging topics now.",
                    "Your positive energy is perfect for group study sessions.",
                    "Consider teaching others - you'll retain information better.",
                    "This is an excellent time for creative problem-solving exercises."
                ],
                'motivational_quotes': [
                    "Success is not the key to happiness. Happiness is the key to success!",
                    "Your positive energy is contagious - keep it up!",
                    "Learning with joy makes knowledge stick better.",
                    "You're in the perfect mindset for growth!"
                ],
                'activities': [
                    "Start a challenging new topic",
                    "Engage in collaborative learning",
                    "Create mind maps or visual aids",
                    "Practice active recall techniques"
                ]
            },
            'sad': {
                'study_tips': [
                    "Start with easier topics to build confidence gradually.",
                    "Take frequent breaks and practice self-compassion.",
                    "Use gentle study methods like reading or listening to lectures.",
                    "Focus on review rather than learning new complex concepts."
                ],
                'motivational_quotes': [
                    "Every expert was once a beginner. You're on your journey.",
                    "It's okay to have difficult days. Progress isn't always linear.",
                    "Small steps forward are still steps forward.",
                    "Your feelings are valid, and so is your potential."
                ],
                'activities': [
                    "Review familiar material",
                    "Listen to educational podcasts",
                    "Do light reading",
                    "Practice mindfulness before studying"
                ]
            },
            'angry': {
                'study_tips': [
                    "Channel your energy into focused study sessions.",
                    "Take deep breaths before starting difficult topics.",
                    "Use physical activity as a study break.",
                    "Practice problem-solving to redirect your intensity."
                ],
                'motivational_quotes': [
                    "Turn your anger into determination for success.",
                    "Strong emotions can fuel strong achievements.",
                    "Channel this energy into breakthrough moments.",
                    "Your intensity can be your greatest asset."
                ],
                'activities': [
                    "Solve challenging problems",
                    "Do intensive review sessions",
                    "Practice with time constraints",
                    "Take active breaks between study sessions"
                ]
            },
            'neutral': {
                'study_tips': [
                    "Perfect state for consistent, steady learning.",
                    "Ideal time for routine study tasks and review.",
                    "Good moment to establish study habits.",
                    "Focus on systematic learning approaches."
                ],
                'motivational_quotes': [
                    "Consistency is the key to mastery.",
                    "Steady progress builds lasting knowledge.",
                    "Your calm focus is a powerful learning tool.",
                    "Balance leads to sustainable success."
                ],
                'activities': [
                    "Follow your regular study routine",
                    "Work through practice problems",
                    "Organize your study materials",
                    "Plan your learning schedule"
                ]
            },
            'fear': {
                'study_tips': [
                    "Start with familiar topics to build confidence.",
                    "Break large tasks into smaller, manageable pieces.",
                    "Use positive self-talk and affirmations.",
                    "Study with others for support and encouragement."
                ],
                'motivational_quotes': [
                    "Courage is not the absence of fear, but action in spite of it.",
                    "Every challenge is an opportunity to grow stronger.",
                    "You are more capable than you realize.",
                    "Fear is temporary, but knowledge lasts forever."
                ],
                'activities': [
                    "Review basics and fundamentals",
                    "Study in a comfortable environment",
                    "Use visualization techniques",
                    "Practice relaxation exercises"
                ]
            },
            'surprise': {
                'study_tips': [
                    "Use this heightened awareness for active learning.",
                    "Great time for exploring new topics or methods.",
                    "Channel curiosity into deep learning.",
                    "Try interactive or hands-on learning approaches."
                ],
                'motivational_quotes': [
                    "Curiosity is the engine of achievement.",
                    "Embrace the unexpected - it leads to discovery.",
                    "Your openness to new ideas is a strength.",
                    "Surprise moments often lead to breakthrough understanding."
                ],
                'activities': [
                    "Explore new learning resources",
                    "Try different study methods",
                    "Engage with interactive content",
                    "Ask questions and seek deeper understanding"
                ]
            },
            'disgust': {
                'study_tips': [
                    "Find ways to make the material more interesting or relevant.",
                    "Connect topics to your personal interests or goals.",
                    "Take breaks and return with a fresh perspective.",
                    "Use different learning formats (videos, podcasts, games)."
                ],
                'motivational_quotes': [
                    "Sometimes the subjects we resist teach us the most.",
                    "Growth happens outside your comfort zone.",
                    "Every topic has value - find the connection that matters to you.",
                    "Push through resistance to discover hidden insights."
                ],
                'activities': [
                    "Find real-world applications of the topic",
                    "Use multimedia learning resources",
                    "Study with others who enjoy the subject",
                    "Reward yourself for completing difficult sections"
                ]
            }
        }
    
    def get_recommendations(self, emotion, stress_level=None):
        """Get personalized recommendations based on emotion and stress level"""
        emotion_lower = emotion.lower()
        
        if emotion_lower not in self.recommendations:
            emotion_lower = 'neutral'  # Default fallback
        
        recs = self.recommendations[emotion_lower]
        
        # Select random items from each category
        selected_tips = random.sample(recs['study_tips'], min(2, len(recs['study_tips'])))
        selected_quotes = random.sample(recs['motivational_quotes'], min(1, len(recs['motivational_quotes'])))
        selected_activities = random.sample(recs['activities'], min(3, len(recs['activities'])))
        
        # Adjust based on stress level if provided
        if stress_level:
            stress_adjustment = self.get_stress_adjustment(stress_level)
            selected_tips.extend(stress_adjustment)
        
        return {
            'emotion': emotion,
            'study_tips': selected_tips,
            'motivational_quote': selected_quotes[0],
            'recommended_activities': selected_activities,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_stress_adjustment(self, stress_level):
        """Get additional recommendations based on stress level"""
        stress_tips = {
            'High': [
                "Take 5-minute breathing breaks every 25 minutes.",
                "Consider shorter study sessions with more frequent breaks.",
                "Practice progressive muscle relaxation before studying."
            ],
            'Medium': [
                "Maintain regular break intervals.",
                "Stay hydrated and take brief walks between sessions.",
                "Use background music if it helps you focus."
            ],
            'Low': [
                "You're in a great state for focused learning!",
                "Consider extending your study sessions slightly.",
                "This is a good time for challenging material."
            ]
        }
        
        return stress_tips.get(stress_level, [])