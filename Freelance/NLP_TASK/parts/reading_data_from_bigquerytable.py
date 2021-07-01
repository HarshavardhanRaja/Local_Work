import argparse
import pandas as pd 
from google.cloud import bigquery


def get_data_frombigquery(project_id, dataset_id, table_id, column_name = '*'):
    """  
    Takes project_id, dataset_id, table_id, column_name as Input.
    column_name is optional if not given returns all the columns from the table
    Retruns a dataframe which contains data from the table. 
    """
    bqclient = bigquery.Client()
    query =( """select {} from `{}.{}.{}`;""".format(column_name, project_id, dataset_id, table_id))
    query_job = bqclient.query(query)
    df = query_job.to_dataframe()
    return df

if __name__ == '__main__':

    # Taking arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-P", "--Project_id", help = "Enter your Project ID", default='gcp-mlops-315308')
    parser.add_argument("-D", "--Dataset_id", help = "Enter your Dataset ID", default='Freelance')
    parser.add_argument("-T", "--Table_id", help = "Enter your Table ID", default='NLP_Task_Input')
    parser.add_argument("-C", "--Column_name", help = "Enter the column_name required", default='*')
    args = parser.parse_args()

    
    print(get_data_frombigquery(args.Project_id, args.Dataset_id, args.Table_id, args.Column_name))

