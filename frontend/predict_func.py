import subprocess
import json
import csv
import pandas as pd
import copy
import numpy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
'''prepared_dataset = []
prepared_dataframe = []
count = 1
while count <= 168:
        query1 = "avg_over_time(container_cpu_usage_seconds_total["+str(count)+"h])"
        call1 = ["curl", "https://datacloud-prometheus.euprojects.net/api/v1/query?query="+query1]
        p1 = subprocess.Popen(call1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output1, err = p1.communicate()
        dict1 = json.loads(output1.decode())
        for i in range(len(dict1["data"]["result"])):
                if ("pod" in dict1["data"]["result"][i]["metric"].keys()):
                        prepared_dataset.append([str("cpu_usage_seconds"),str(count),str(dict1["data"]["result"][i]["metric"]["pod"]),str(dict1["data"]["result"][i]["metric"]["instance"]),str(float(dict1["data"]["result"][i]["value"][1]))])
        count = count + 1
prepared_dataframe = pd.DataFrame(prepared_dataset, columns=["metric","hour(s)_ago","pod","instance","value"])
#print(prepared_dataframe)

count = 1
while count <= 168:
        query1 = "avg_over_time(container_memory_usage_bytes["+str(count)+"h])"
        call1 = ["curl", "https://datacloud-prometheus.euprojects.net/api/v1/query?query="+query1]
        p1 = subprocess.Popen(call1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output1, err = p1.communicate()
        dict1 = json.loads(output1.decode())
        for i in range(len(dict1["data"]["result"])):
                if ("pod" in dict1["data"]["result"][i]["metric"].keys()):
                        prepared_dataset.append([str("memory_usage_MiB"),str(count),str(dict1["data"]["result"][i]["metric"]["pod"]),str(dict1["data"]["result"][i]["metric"]["instance"]),str(float(dict1["data"]["result"][i]["value"][1])/1024/1024)])
        count = count + 1
prepared_dataframe = pd.DataFrame(prepared_dataset, columns=["metric","hour(s)_ago","pod","instance","value"])
prepared_dataframe.to_csv('dataset_cpu_mem-v1.csv')'''
df1 = []
with open(r'dataset_cpu_mem-v1.csv', 'r') as file1:
    reader_obj = csv.reader(file1)
    with open('container-new.csv', 'w') as file2:
        writer = csv.writer(file2)
        for row in reader_obj:
            if(row[1]=="cpu_usage_seconds" and "demo-" in row[3]):
                writer.writerow([copy.copy(row[2]),copy.copy(row[3]),copy.copy(row[5])])
with open('container-new-new.csv', 'w') as file3:
    writer = csv.writer(file3)
    writer.writerow(["hour(s)_ago","pod","value_cpu","value_mem"])
    with open(r'dataset_cpu_mem-v1.csv', 'r') as file1:
        reader_obj = csv.reader(file1)
        for row in reader_obj:
            with open(r'container-new.csv', 'r') as file2:
                reader_obj2 = csv.reader(file2)
                for row2 in reader_obj2:
                    row_new = copy.copy(row2)
                    if (row[1]=="memory_usage_MiB" and row[2]==row_new[0] and row[3]==row_new[1]):
                        row_new.append(row[5])
                        writer.writerow(row_new)

# read the CSV file into a Pandas dataframe
df1 = pd.read_csv(r'container-new-new.csv')

df2 = pd.DataFrame(df1,columns=["value_cpu","value_mem"])

#df1 = df1.reset_index(drop=True, inplace=True)

# drop duplicate rows from dataframe
#df1 = df1.drop_duplicates()

#df2.to_csv('demo_containers_with_cpu_memory.csv')
#print(df2.head())

# dataset
dataset = df2.values
X = dataset[:, 0] # cpu column
#print(numpy.min(X)," ",numpy.max(X))
#print(len(X))
Y = dataset[:, 1] # mem column
#print(numpy.min(Y)," ",numpy.max(Y))
#print(len(Y))

X = X.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)
#print("Train: ", X_train.shape)
#print("Val: ", X_val.shape)
#print("Test: ", X_test.shape)

# model
gbr = GradientBoostingRegressor(subsample=0.8,
                                learning_rate=0.4,
                                n_estimators=14,
                                max_depth=40,
                                min_samples_split=200,
                                min_samples_leaf=40,
                                loss="absolute_error")

# fit
gbr.fit(X_train, Y_train)

# prediction
Y_predict = gbr.predict(X_test)

#from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
mae = mean_absolute_error(Y_test, Y_predict)
mape = mean_absolute_percentage_error(Y_test, Y_predict)
#print("MAPE : ", mape)
#print("MAE : ", mae)

replica_actual = []
for i in range(len(X_test)):
    replica_actual.append(numpy.ceil(X_test[i]/Y_test[i]))

replica_gbr = []
for i in range(len(X_test)):
    replica_gbr.append(numpy.ceil(X_test[i]/Y_predict[i]))

#print(numpy.array(replica_gbr))
df1['replica']=numpy.ones((len(Y)))
#df1.to_csv('demo_containers_with_cpu_memory.csv')
#print(df1.head())
prepared_dataframe = []
prepared_dataframe = df1.copy()
