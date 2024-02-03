# imports
from transformers import pipeline

# TODO - DEFINE YOUR FEATURE EXTRACTOR HERE
pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis", top_k=None)
def get_sentiment(text):    
    # sample output format
    result = pipe(text)
    pos = [score['score'] for score in result[0] if score['label'] == 'POS'][0]
    neg = [score['score'] for score in result[0] if score['label'] == 'NEG'][0]
    neu = [score['score'] for score in result[0] if score['label'] == 'NEU'][0]
    return({'positive': pos, 'negative': neg, 'neutral': neu})