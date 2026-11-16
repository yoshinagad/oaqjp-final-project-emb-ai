'''Analyze the text.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    response_str = str(response)
    if response['dominant_emotion'] is None:
        return '<b>Invalid text! Please try again!</b>'

    ret_val = "For the given statement, the system response is {}. "
    ret_val += "The dominant emotion is <b>{}</b>"
    return ret_val.format(response_str[1:-1],response['dominant_emotion'])

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
