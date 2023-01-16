import sys
sys.path.append('./parser_constants')
from parser_constants import *
import json


def parseDSL (in_file) -> None:
    count = 0
    #with open(in_file, "r") as fp:
        #while line := in_file.readline():
    for line in in_file.splitlines():    
            with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json', 'r') as openfile:
                requirement_settings = json.load(openfile)

            #words = line.strip().split(" ")
            words = line.split(' ')
            
            if  len(words) != 1:
                if (words[0] == STEPS_REQ_MAXCPU):
                    requirement_settings["stepsList"][0]["requirement"]["vCPUs"]=((float(words[1]))/1024.0)
                    
                elif (words[0] == STEPS_REQ_MINMEM):
                    requirement_settings["stepsList"][0]["requirement"]["ram"] = words[1]
                    
                elif (words[0] == STEPS_IMPLEMENTATION):
                    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
                    
    
            if (count == 0):
                requirement_settings["stepsList"][0]["provider"] = "Tellu" 
                requirement_settings["stepsList"][0]["resource"] = "Tellu Gateway 0" 
            else:
                requirement_settings["stepsList"][0]["provider"] = "DataCloud-k8s"
                requirement_settings["stepsList"][0]["resource"] = "DataCloud-k8s-1"
                
            if "data-processing step" in line or "data-source step" in line:
                count += 1

    with open("D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json", "w") as outfile:
                json.dump(requirement_settings,outfile)


###Loading the DSL from GitHub###
#from subprocess import call
#call(["Invoke-WebRequest","-URI","https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/tellu.dsl","-OutFile","tellu.dsl"])
#in_file = "D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\tellu.dsl"
#parseDSL (in_file)

###Getting the pipeline definition with the help of the access token### 
#import os
#cmd = "curl -X \'GET\' \'https://crowdserv.sys.kth.se/api/repo/export/testuser/pipeline\' -H \'accept: text/plain\'  -H \'Authorization: Bearer TTOOKKEENN'"
#command = str.encode(os.popen(cmd).read())
#output = command.decode()
output = "{\"data\":\"Pipeline pipeline {\n\tcommunicationMedium: medium \n\tsteps:\n\t\t- data-processing step Data_Analysis\n\t\t\timplementation: container-implementation image: \'\'\n\t\t\tenvironmentParameters: {\n\n\t\t\t}\n\t\t\tresourceProvider: \n\t\t\texecutionRequirement:\n\t\t\t\thardRequirements:\t\t\t\t\t\n\n\n\t\t- data-processing step Scenarios_Generation\n\t\t\timplementation: container-implementation image: \'what-if docker\'\n\t\t\tenvironmentParameters: {\n\n\t\t\t}\n\t\t\tresourceProvider: \n\t\t\texecutionRequirement:\n\t\t\t\thardRequirements:\t\t\t\t\t\n\t\t\t\t\thorizontalScale:\n\t\t\t\t\t\tmin-instance: 1\n\t\t\t\t\t\tmax-instance: 1000\n\n\n\t\t- data-processing step Production_Workflow_Simulation\n\t\t\timplementation: container-implementation image: \'what-if docker'\n\t\t\tenvironmentParameters: {\n\n\t\t\t}\n\t\t\tresourceProvider: \n\t\t\texecutionRequirement:\n\t\t\t\thardRequirements:\t\t\t\t\t\n\t\t\t\t\thorizontalScale:\n\t\t\t\t\t\tmin-instance: 1\n\t\t\t\t\t\tmax-instance: 1000\n\n\n\t\t- data-processing step What-if_Analysis\n\t\t\timplementation: container-implementation image: 'what-if docker'\n\t\t\tenvironmentParameters: {\n\n\t\t\t}\n\t\t\tresourceProvider: \n\t\t\texecutionRequirement:\n\t\t\t\thardRequirements:\t\t\t\t\t\n\t\t\t\t\thorizontalScale:\n\t\t\t\t\t\tmin-instance: 1\n\t\t\t\t\t\tmax-instance: 1000\n\n}\n\nCloudProvider Cloud Service {\n\tproviderLocation: \'x\'\n\tmappingLocation: \'x\'\n}\n\nEdgeProvider 2nd {\n\tproviderLocation: 'aa'\n\tmappingLocation: \'aa\'\n}\",\"success\":true,\"errorMessage\":null}"

output=output.replace("\\n","")
output=output.replace("\\t","")
parseDSL (output)
