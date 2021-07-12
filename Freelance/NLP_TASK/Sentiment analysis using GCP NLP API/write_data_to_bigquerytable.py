



import pandas as pd 
from google.cloud import bigquery

def write_to_bigquery(data, project_id, dataset_id, output_table_id):
    """
    Takes dataframe, project_id, dataset_id, table_id as input 
    Writes the data in dataframe to the table provided
    """
    data.to_gbq('{}.{}'.format(dataset_id, output_table_id), 
                '{}'.format(project_id),
                chunksize=None, 
                if_exists='replace')

