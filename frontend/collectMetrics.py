'''import time
import numpy
import pandas as pd
import copy
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect()

prepared_dataset = []
prepared_dataframe = []

avg_cpu = 0
## grab cpu percentage
query_cpu = prom.custom_query(query="netdata_cpu_cpu_percentage_average")
for i in range(len(query_cpu)):
        prepared_dataset.append([query_cpu[i]["metric"]["instance"],query_cpu[i]["metric"]["chart"],numpy.round(float(query_cpu[i]['value'][1]),5)])


## grab system mem percentage
query_mem2 = prom.custom_query(query="netdata_system_ram_MiB_average")
for i in range(len(query_mem2)):
        prepared_dataset.append([query_mem2[i]["metric"]["instance"],query_mem2[i]["metric"]["chart"],numpy.round(float(query_mem2[i]['value'][1]),5)])

## grab storage percentage
query_disk = prom.custom_query(query="netdata_disk_space_GiB_average{family=\"/\"}")
for i in range(len(query_disk)):
        prepared_dataset.append([query_disk[i]["metric"]["instance"],query_disk[i]["metric"]["chart"],numpy.round(float(query_disk[i]['value'][1]),5)])

## grab service mem percentage
query_mem = prom.custom_query(query="netdata_services_mem_usage_MiB_average")
for i in range(len(query_mem)):
        prepared_dataset.append([query_mem[i]["metric"]["instance"],query_mem[i]["metric"]["dimension"],numpy.round(float(query_mem[i]['value'][1]),5)])
'''
import subprocess
import json
import csv
import pandas as pd
#import numpy
prepared_dataset = []
prepared_dataframe = []
count = 1
while count <= 10:
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
while count <= 10:
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

