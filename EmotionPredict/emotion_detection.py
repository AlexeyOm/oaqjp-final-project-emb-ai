import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    ''' Function uses Watson NLP API to return emotions score and dominant emotions name
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    formatted_response = json.loads(response.text)

    emotions_dict = formatted_response["emotionPredictions"][0]["emotion"]    # getting the scores the emotions and their scores

    scores_dict = {v: k for k, v in emotions_dict.items()} # inverting the emotions and scores
    max_scores = max([v for _, v in emotions_dict.items()]) # finding the maximum score value

    emotions_dict["dominant_emotion"] = scores_dict[max_scores]

    return emotions_dict
