import argparse
import pandas as pd
from google.cloud import language


def analyze_text_sentiment(text):
    """
    Takes text as an Input
    Returns a list which contains text, score, magnitude respectively for the text obtained from google's NLP API
    """
    client = language.LanguageServiceClient.from_service_account_json('../nlp-api-task-auth.json')

    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment

    return  list([text,"{}".format(sentiment.score), "{}".format(sentiment.magnitude)])

if __name__ == '__main__':

    # Taking arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-T", "--Text", help = "Enter text for sentiment analysis", default='gcp-mlops-315308')
    args = parser.parse_args()
 
    print(analyze_text_sentiment(args.Text))