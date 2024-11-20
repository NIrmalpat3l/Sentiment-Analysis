# sentiment_model.py
from transformers import pipeline

# Load pre-trained sentiment-analysis pipeline
nlp = pipeline('sentiment-analysis')

def predict_sentiment(text):
    result = nlp(text)[0]
    return result



