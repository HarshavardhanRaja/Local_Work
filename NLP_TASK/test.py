import pandas as pd 
from google.cloud import bigquery
from google.cloud import language

def get_data_frombigquery(project_id, dataset_id, table_id):
    """  
    Takes project_id, dataset_id and table_id as Input.
    Retruns a dataframe which contains data from the table. 
    """
    bqclient = bigquery.Client()

    query =( """select * from `{}.{}.{}`;""".format(project_id, dataset_id, table_id))
    query_job = bqclient.query(query)
    df = query_job.to_dataframe()

    return df

def analyze_text_sentiment(text):
    """
    Takes text as an Input
    Returns a dictonary which contains text, score, magnitude for the text obtained from google's NLP API
    """
    client = language.LanguageServiceClient()

    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score="{}".format(sentiment.score),
        magnitude="{}".format(sentiment.magnitude),
                )

    return results





if __name__ == '__main__':
    # parameters
    project_id = 'gcp-mlops-315308'
    dataset_id = 'Freelance'
    input_table_id = 'NLP_Task_Input'
    output_table_id = 'NLP_Task_Output'


    data = get_data_frombigquery(project_id, dataset_id, input_table_id)
    output_data = pd.DataFrame()
    for i in data.index:
        results = analyze_text_sentiment(str(data['Comment'][i]))
        output_data = output_data.append(results, ignore_index=True)
    
    # stores dictonaries obtained from analyze_text_sentiment() to a pandas dataframe 
    # The data from the above dataframe is loaded into the bigquery output table
    output_data.to_gbq('{}.{}'.format(dataset_id, output_table_id), 
                 '{}'.format(project_id),
                 chunksize=None, 
                 if_exists='append'
                 )
    print('Finish')


    



