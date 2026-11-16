import requests, json

def emotion_detector(text_to_analyze):
    URL ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_JSON = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json = INPUT_JSON, headers = HEADERS)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_value = 0
        dominant_key = ''
        for key, value in emotions.items():
            if value > dominant_value:
                dominant_key = key
                dominant_value = value

        emotions["dominant_emotion"] = dominant_key

        return emotions

    elif response.status_code == 400:
        return {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
