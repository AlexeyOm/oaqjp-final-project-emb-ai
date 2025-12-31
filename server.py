''' Server for Flask-based emotions detection applications
'''
from flask import Flask, render_template, request
from EmotionPredict.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and relative  
        scores for the provided text, as well as dominant_emotion
    '''
    try:
        text_to_analyze = request.args.get("textToAnalyze")
        response = emotion_detector(text_to_analyze)
        dominant_emotion = response["dominant_emotion"]
        if dominant_emotion is None:
            return "<b>Invalid text! Please try again!</b>"
        emotion_list = [f"'{k}': {v}" for k, v in response.items()]
        response_text = 'For the given statement, the system response is  ' \
            f'{", ".join(emotion_list[:-2])} and {"".join(emotion_list[-2:-1])}.' \
            f'The dominant emotion is <b>{dominant_emotion}</b>'
        return response_text
    except KeyError:
        return "Invalid input ! try again"

    return ("Something bad happend on the server", 500)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

# pylint: disable=pointless-string-statement
if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000,  use_reloader=True)
