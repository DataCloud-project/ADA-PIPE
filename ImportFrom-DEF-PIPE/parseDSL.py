import sys
sys.path.append('./interface_constants')
from interface_constants import *
import json
from typing import List, Dict
from copy import copy, deepcopy
import yaml


inFile = "D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\tellu.dsl"

with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json', 'r') as openfile:
			requirement_settings = json.load(openfile)
			openfile.close

count = 0
with open(inFile, "r") as fp:
    while True:
        
        line = fp.readline()
        if not line:
            break
        
        words = line.strip().split(" ")
        
        if  len(words) != 1:
            if (words[0] == STEPS_REQ_MAXCPU):
                requirement_settings["stepsList"][0]["requirement"]["vCPUs"]=((float(words[1]))/1024.0)
                #print(requirement_settings["stepsList"][0]["requirement"]["vCPUs"])
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][0]["requirement"]["ram"] = words[1]
                #print(requirement_settings["stepsList"][0]["requirement"]["ram"])
            elif (words[0] == STEPS_IMPLEMENTATION):
                requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
                #print(requirement_settings["stepsList"][0]["dockerImage"])
 
        if (count == 0):
            requirement_settings["stepsList"][0]["provider"] = "Tellu" 
            requirement_settings["stepsList"][0]["resource"] = "Tellu Gateway 0" 
        else:
            requirement_settings["stepsList"][0]["provider"] = "DataCloud-k8s"
            requirement_settings["stepsList"][0]["resource"] = "DataCloud-k8s-1"
            
        if  "data-processing step" in line  or  "data-source step" in line:
            count += 1
        #print(count)
with open("D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json", "w") as outfile:
			json.dump(requirement_settings,outfile)
			outfile.close
#with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\requirements.yaml', 'r') as file_read:
#	requirement_list = yaml.load(file_read, Loader=yaml.FullLoader)#json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))
#print((requirement_list))
