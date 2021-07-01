import pandas as pd
from reading_data_from_bigquerytable import get_data_frombigquery
from write_data_to_bigquerytable import write_to_bigquery
from sentiment_analysis_from_nlpapi import analyze_text_sentiment




if __name__ == "__main__":
    # parameters
    project_id = 'gcp-mlops-315308'
    dataset_id = 'Freelance'
    input_table_id = 'NLP_Task_Input'
    output_table_id = 'NLP_Task_Input'
    column_name = 'Comment'

    # get data from a bigquery table to a dataframe
    df = get_data_frombigquery(project_id, dataset_id, input_table_id)

    # for each row in dataframe pass the column which contains the text to analyze_text_sentiment function
    # Then add sentiment_score, sentiment_magnitude columns to the dataframe
    score = []
    magnitude = []
    for index, row in df.iterrows():
        result = analyze_text_sentiment(row[column_name])
        score.append(result[1])
        magnitude.append(result[2])
    df['sentiment_score'] = score
    df['sentiment_magnitude'] = magnitude

    # write to updated dataframe back to biguery table
    write_to_bigquery(df, project_id, dataset_id, output_table_id )
    print('Check the bigquery table for the results from NLP API')



