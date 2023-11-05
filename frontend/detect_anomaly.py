import json
import csv
import pandas as pd
# read the CSV file into a Pandas dataframe
prepared_dataset = pd.read_csv(r'device_anomaly.csv')

prepared_dataframe = pd.DataFrame(prepared_dataset)



