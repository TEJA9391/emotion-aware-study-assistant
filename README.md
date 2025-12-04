# 🧠 Emotion-Aware Study Assistant

An intelligent AI-powered study companion that monitors your emotional state and facial expressions in real-time to optimize your learning experience. Built with Flask, OpenCV, and modern web technologies.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 🎭 Emotion Detection
- **Real-time facial emotion recognition** using advanced CV models
- Detects 7 emotions: Happy, Sad, Angry, Surprised, Neutral, Fear, Disgust
- Continuous monitoring and analysis during study sessions

### 🎤 Voice Analysis
- Speech-to-text transcription
- Emotion detection from voice tone and patterns
- Voice command support for hands-free control

### 📊 Study Session Analytics
- Track your focus levels over time
- Detailed emotion history and patterns
- Session duration and productivity metrics
- Visual charts and insights

### 🎯 Smart Recommendations
- Personalized study tips based on your emotional state
- Break reminders when stress is detected
- Motivational support during low-energy periods

### 🎨 Modern UI/UX
- Clean, responsive design
- Gradient backgrounds and smooth animations
- Real-time emotion display with emoji indicators
- Mobile-friendly interface

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
pip (Python package manager)
Webcam (for face detection)
Microphone (for voice analysis)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/TEJA9391/emotion-aware-study-assistant.git
cd emotion-aware-study-assistant
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
```
Navigate to: http://localhost:5000
```

## 📦 Dependencies

- **Flask** - Web framework
- **OpenCV (cv2)** - Computer vision and face detection
- **fer** - Facial Emotion Recognition
- **SpeechRecognition** - Voice to text conversion
- **NumPy** - Numerical computations
- **Additional libraries**: See `requirements.txt`

## 🎯 Usage

1. **Start a Study Session**
   - Click "Start Studying" on the home page
   - Grant camera and microphone permissions when prompted

2. **Monitor Your Emotions**
   - Your current emotion is displayed in real-time
   - View emotion history in the sidebar
   - Check focus levels and analytics

3. **Use Voice Commands**
   - Click the microphone icon to activate voice input
   - Say commands like "take a break" or "how am I doing?"

4. **End Session**
   - Click "End Session" to view your complete study analytics
   - Review recommendations for future sessions

## 📸 Screenshots

### Main Study Interface
The clean, modern interface displays real-time emotion detection with smooth animations.

### Analytics Dashboard
Track your emotional patterns and study effectiveness over time.

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend logic |
| Flask | Web framework |
| OpenCV | Face detection |
| FER | Emotion recognition |
| HTML/CSS/JS | Frontend interface |
| Chart.js | Data visualization |
| SpeechRecognition | Voice analysis |

## 📁 Project Structure

```
emotion-aware-study-assistant/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Main UI template
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   └── js/
│       └── script.js      # Frontend logic
└── README.md              # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**TEJA9391**
- GitHub: [@TEJA9391](https://github.com/TEJA9391)
- Email: tejrtej9347@gmail.com

## 🙏 Acknowledgments

- FER library for emotion recognition
- OpenCV community
- Flask framework developers

## 🔮 Future Enhancements

- [ ] Machine learning model for personalized recommendations
- [ ] Multi-user support with profiles
- [ ] Mobile app version
- [ ] Integration with calendar and task management
- [ ] Advanced analytics with ML insights
- [ ] Export study reports to PDF

---

⭐ If you find this project helpful, please consider giving it a star!

**Made with ❤️ by TEJA9391**
