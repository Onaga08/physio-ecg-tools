import os
import wfdb
import csv
from pandas import read_csv
import pandas as pd 

data = read_csv("metadata.csv")

ecg_datasets = data['Name'].tolist()

datapoints = []
for db in ecg_datasets:
    recordlist = wfdb.io.get_record_list(db)
    num_datapoints = len(recordlist)
    datapoints.append(num_datapoints)

data['No of Datapoints'] = datapoints
data.to_csv("metadata.csv", index=False)

