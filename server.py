from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion():

    text = request.args.get("textToAnalyze")

    if text is None or text == "":
        return "Invalid input"

    result = emotion_detector(text)

    if result is None:
        return "Invalid text! Please try again."

    return str(result)


if __name__ == "__main__":
    app.run()