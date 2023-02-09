import time
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

prepared_dataframe = pd.DataFrame(prepared_dataset, columns=["instance","metric","value"])
#print(prepared_dataframe)
#from flask import jsonify
#print((prepared_dataframe.values.tolist()))
