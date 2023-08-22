import numpy
from operator import itemgetter
import yaml
import json
import os
import warnings
warnings.filterwarnings('ignore')

alloc_total = []

def Cost_opt_match(DCPipelines, resources, Time, Cost):
	lenn_app = len(DCPipelines)
	dictlistResources = list( {} for i in range(len(resources)) )
	sorted_dictlistResources = list( {} for i in range(len(resources)) )
	dictlistmicros = list( {} for i in range(lenn_app) )  #####
	sorted_dictlistmicros = list( {} for i in range(lenn_app) ) #####
	fileObject = open("./APL.yaml", 'w').close()
	capfile = open('./capacities-testbed.yml', 'w').close()
	fileObject2 = open("./IPL.yaml",'w').close()

	alloc = [0  for j in range(lenn_app)] 
	for i in range(lenn_app):
			for j in range(len(resources)):
				#print(i, " ",  DCPipelines[i],"  ", j ," ",resources[j])
				#print(dictlistmicros[i])
				dictlistmicros[i][(resources[j],DCPipelines[i])] = Time[i][j]
			sorted_dictlistmicros[i]=sorted(dictlistmicros[i].items(),key = itemgetter(1), reverse=False)
			mpllll=dict(dict(sorted_dictlistmicros[i]).keys())
			listofvalues = list(mpllll.keys())
			listofkeys=list(mpllll.values())
			dicttttt= {listofkeys[0]:listofvalues}
			with open(r'./APL.yaml', 'a') as file:
				documents = yaml.dump(dicttttt, file)
				file.close()

	dictlistResources = list( {} for i in range(len(resources)) )
	sorted_dictlistResources = list( {} for i in range(len(resources)) )
	for j in range(len(resources)):
				#print(DCPipelines[i],"  ",resources[j],"  ")
				for i in range(lenn_app):
					dictlistResources[j][(DCPipelines[i],resources[j])] =(Cost[i][j])
				sorted_dictlistResources[j] = sorted(dictlistResources[j].items(),key = itemgetter(1), reverse=False)
				dpllll = dict(dict(sorted_dictlistResources[j]).keys())
				listofvalues = list(dpllll.keys())
				listofkeys = list(dpllll.values())
				dicttttt = {listofkeys[0]:listofvalues}
				with open(r'./IPL.yaml', 'a') as file:
						documents = yaml.dump(dicttttt, file)
						file.close()
				capacity_dict = {listofkeys[0]:1}
				with open(r'./capacities-testbed.yml', 'a') as capfile:
						yaml.dump(capacity_dict, capfile)
						file.close()
			########################-----------------------------------------------------------------------------------------------------------------------------################
	command = str.encode(os.popen("python3 "+"./matching-code.py").read())
	command.decode()
	with open('./matching-yaml.yaml', 'r') as file_read:
				# The FullLoader parameter handles the conversion from YAML
				# scalar values to the dictionary format
				matching_list = yaml.load(file_read, Loader=yaml.FullLoader)
				file_read.close()
				dataa = json.loads(matching_list)
				for ind in range(len(dataa)):
					for key, values in dataa[ind].items():
							#print(values, " ", (key))
							for value in ((values)):
								for appp in range(lenn_app):
									if (value == (DCPipelines[appp])):
										alloc[appp] = resources.index(key)
	#print (alloc)
	counter_cost_model = [0, 0, 0, 0, 0]
	sum_cost_cost_user_rank = 0
	sum_cost_time_user_rank = 0
	#print()
	for i in range(lenn_app):
		counter_cost_model[alloc[i]] = counter_cost_model[alloc[i]] + 1
		sum_cost_time_user_rank = sum_cost_time_user_rank + Time[i][alloc[i]]
		sum_cost_cost_user_rank = sum_cost_cost_user_rank + Cost[i][alloc[i]]
	alloc_total.append(alloc)
	return sum_cost_cost_user_rank,sum_cost_time_user_rank

DCPipelines = {
    "pipeline": [
		{
			"name" : "tellu",
			"step" : ["dcgenerate", "dcreceive", "dcnotification"],
			"core" : [1, 2, 4]
		},
		{
			"name" : "mog",
			"step" : ["detection", "fusion", "overlay"],
			"core" : [1, 4, 4]
		},
		{
			"name" : "jot",
			"step" : ["DataCleaning_Conv", "DataCleaning_Stats", "DataCleaning_Rev"],
			"core" : [2, 1, 1] 
		},
		{
			"name" : "ceramica",
			"step" : ["Data_Analysis", "Digital_Twins", "What-If_Analysis"],
			"core" : [2, 4, 4]
		},
		{
			"name" : "bosch",
			"step" : ["dataretrieve", "dataslice", "dataprocess"],
			"core" : [4, 4, 4]
		}
	]
}

lenn_app = len(DCPipelines["pipeline"])

resources = ["e2-medium", "c5a.xlarge", "c5.xlarge", "c5a.2xlarge", "c5.2xlarge"]
resources_cores = [2, 4, 4, 8, 8]
#2, 4GB
#4,	8GB
#4,	8GB
#8,	16GB
#8,	16GB

#cost_per_sec = numpy.array([0.038795, 0.182, 0.202, 0.364, 0.404])
#print(cost_per_sec/3600)
cost_per_sec = numpy.array([1.07763889e-05, 5.05555556e-05, 5.61111111e-05, 1.01111111e-04, 1.12222222e-04])

Time = [[[0 for k in range(len(resources))] for j in range(len(DCPipelines["pipeline"][0]["step"]))] for i in range(len(DCPipelines["pipeline"]))]
Cost = [[[0 for k in range(len(resources))] for j in range(len(DCPipelines["pipeline"][0]["step"]))] for i in range(len(DCPipelines["pipeline"]))]


for i in range(numpy.shape(Time)[0]):
	for j in range(numpy.shape(Time)[1]):
		for k in range(numpy.shape(Time)[2]):
			Time[i][j][k] = DCPipelines["pipeline"][i]["core"][j] / resources_cores[k]
			Cost[i][j][k] = Time[i][j][k]*cost_per_sec[k]
			#print(DCPipelines["pipeline"][j]["core"][j], " ", resources_cores[k])
			#print(Cost[i][j][k], "   ")
		#print()
	#print()

for i in range(numpy.shape(Time)[0]):
		#print(DCPipelines["pipeline"][i]["step"])
		#print(numpy.shape(Time[i][:]), "  ", numpy.shape( Cost[i][:]))
		sum_cost_cost_user_rank,sum_cost_time_user_rank = Cost_opt_match(DCPipelines["pipeline"][i]["step"], resources, Time[i][:], Cost[i][:])
		print(DCPipelines["pipeline"][i]["name"], "... \tCost (EUR): ",numpy.round(sum_cost_cost_user_rank*3600,4), "... \tTime (sec): ", sum_cost_time_user_rank)