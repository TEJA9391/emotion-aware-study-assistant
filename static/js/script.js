let videoStream = null;
let isAnalyzing = false;

// Start emotion analysis using webcam
async function startEmotionAnalysis() {
    try {
        // Show loading modal
        document.getElementById('loading-modal').style.display = 'flex';

        // Request webcam access
        videoStream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        // Create video element
        const video = document.createElement('video');
        video.srcObject = videoStream;
        video.play();

        isAnalyzing = true;

        // Wait for video to be ready
        video.onloadedmetadata = () => {
            // Capture frame after 2 seconds
            setTimeout(() => {
                captureAndAnalyze(video);
            }, 2000);
        };

    } catch (error) {
        console.error('Error accessing webcam:', error);
        alert('Error accessing webcam. Please ensure you have granted camera permissions.');
        document.getElementById('loading-modal').style.display = 'none';
    }
}

// Capture frame and send for analysis
function captureAndAnalyze(video) {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    // Convert to base64
    const imageData = canvas.toDataURL('image/jpeg');

    // Send to server
    fetch('/analyze_emotion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageData })
    })
        .then(response => response.json())
        .then(data => {
            displayEmotionResults(data);
            stopVideoStream();
            document.getElementById('loading-modal').style.display = 'none';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error analyzing emotion: ' + error.message);
            stopVideoStream();
            document.getElementById('loading-modal').style.display = 'none';
        });
}

// Display emotion results
function displayEmotionResults(data) {
    const resultsSection = document.getElementById('results-section');
    const emotionResults = document.getElementById('emotion-results');

    if (data.success) {
        const emotionEmojis = {
            'happy': '😊',
            'sad': '😢',
            'angry': '😠',
            'surprise': '😲',
            'neutral': '😐',
            'fear': '😨',
            'disgust': '🤢'
        };

        const emoji = emotionEmojis[data.emotion] || '😐';
        const confidence = (data.confidence * 100).toFixed(1);

        let html = `
            <div class="emotion-card">
                <div class="emotion-emoji">${emoji}</div>
                <h3>Detected Emotion: ${data.emotion}</h3>
                <p class="confidence">Confidence: ${confidence}%</p>
                
                <div class="all-emotions">
                    <h4>All Emotions:</h4>
                    <div class="emotion-bars">
        `;

        for (const [emotion, value] of Object.entries(data.all_emotions)) {
            const percentage = (value * 100).toFixed(1);
            html += `
                <div class="emotion-bar">
                    <span class="emotion-label">${emotion}</span>
                    <div class="bar-container">
                        <div class="bar-fill" style="width: ${percentage}%"></div>
                    </div>
                    <span class="emotion-value">${percentage}%</span>
                </div>
            `;
        }

        html += `
                    </div>
                </div>
            </div>
        `;

        emotionResults.innerHTML = html;

        // Display recommendations
        if (data.recommendations) {
            displayRecommendations(data.recommendations, data.quote);
        }

        resultsSection.style.display = 'block';
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    } else {
        emotionResults.innerHTML = `
            <div class="error-message">
                <p>${data.message || 'No face detected. Please try again.'}</p>
            </div>
        `;
        resultsSection.style.display = 'block';
    }
}

// Display recommendations
function displayRecommendations(recommendations, quote) {
    const recommendationsResults = document.getElementById('recommendations-results');

    let html = `
        <div class="recommendations-card">
            <h3>Personalized Recommendations</h3>
            ${quote ? `<blockquote class="quote">"${quote}"</blockquote>` : ''}
            <ul class="recommendations-list">
    `;

    recommendations.forEach(rec => {
        html += `<li>${rec}</li>`;
    });

    html += `
            </ul>
        </div>
    `;

    recommendationsResults.innerHTML = html;
}

// Start voice analysis
async function startVoiceAnalysis() {
    try {
        document.getElementById('loading-modal').style.display = 'flex';
        document.querySelector('#loading-modal p').textContent = 'Recording your voice... Please speak';

        // Request microphone access
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const mediaRecorder = new MediaRecorder(stream);
        const audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const formData = new FormData();
            formData.append('audio', audioBlob, 'recording.wav');

            try {
                const response = await fetch('/analyze_voice', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();
                displayVoiceResults(data);
            } catch (error) {
                console.error('Error:', error);
                alert('Error analyzing voice: ' + error.message);
            }

            document.getElementById('loading-modal').style.display = 'none';
            stream.getTracks().forEach(track => track.stop());
        };

        mediaRecorder.start();

        // Record for 5 seconds
        setTimeout(() => {
            if (mediaRecorder.state === 'recording') {
                mediaRecorder.stop();
            }
        }, 5000);

    } catch (error) {
        console.error('Error accessing microphone:', error);
        alert('Error accessing microphone. Please ensure you have granted microphone permissions.');
        document.getElementById('loading-modal').style.display = 'none';
    }
}

// Display voice results
function displayVoiceResults(data) {
    const resultsSection = document.getElementById('results-section');
    const voiceResults = document.getElementById('voice-results');

    if (data.success) {
        const html = `
            <div class="voice-card">
                <h3>Voice Analysis Results</h3>
                <p><strong>Detected Emotion:</strong> ${data.emotion}</p>
                ${data.text ? `<p><strong>Transcribed Text:</strong> "${data.text}"</p>` : ''}
                <p><strong>Confidence:</strong> ${(data.confidence * 100).toFixed(1)}%</p>
            </div>
        `;

        voiceResults.innerHTML = html;
        resultsSection.style.display = 'block';
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    } else {
        voiceResults.innerHTML = `
            <div class="error-message">
                <p>Error analyzing voice. Please try again.</p>
            </div>
        `;
        resultsSection.style.display = 'block';
    }
}

// Stop analysis
function stopAnalysis() {
    isAnalyzing = false;
    stopVideoStream();
    document.getElementById('loading-modal').style.display = 'none';
}

// Stop video stream
function stopVideoStream() {
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
        videoStream = null;
    }
}
