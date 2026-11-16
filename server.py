from flask import Flask, request, render_template, json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    textToAnalyze = request.args.get('textToAnalyze')
    response = emotion_detector(textToAnalyze)
    response_str = str(response)
    if response['dominant_emotion'] == None:
        return '<b>Invalid text! Please try again!</b>'

    return "For the given statement, the system response is {}.  The dominant emotion is <b>{}</b>".format(response_str[1:-1],response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')