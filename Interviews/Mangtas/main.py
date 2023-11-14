import pandas as pd

def get_driver_performance(file_path, from_date, to_date, top_n_drivers):
    """
    This function is to return top 10 drivers based on their performance
    """

    df = pd.read_csv(file_path)
    driver_performance = {}
    for row in df.iterrows():
        if row['driver'] in driver_performance.keys():
            if from_date < row['date'] < to_date:
                driver_performance[row['driver']] += row['duration']
        else:
            if from_date < row['date'] < to_date:
                driver_performance[row['driver']] = row['duration']

    performance_df = pd.Dataframe(driver_performance, columns=['driver_id', 'total_duration'])
    performance_df.sort_values(by=['total_duration'], ascending=False)

    return performance_df.head(top_n_drivers)
