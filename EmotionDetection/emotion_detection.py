import requests


def emotion_detector(text_to_analyze):

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/"
        "NlpService/EmotionPredict"
    )

    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    json_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:

        response = requests.post(
            url,
            json=json_data,
            headers=header,
            timeout=10
        )

    except Exception:

        return {
            "anger": 0,
            "joy": 0,
            "sadness": 0,
            "fear": 0,
            "disgust": 0
        }

    if response.status_code == 400:
        return None

    formatted = response.json()

    emotions = formatted[
        "emotionPredictions"
    ][0]["emotion"]

    return emotions