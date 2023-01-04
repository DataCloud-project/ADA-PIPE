import sys
sys.path.append('./parser_constants')
from parser_constants import *
import json

def parseDSL (in_file) -> None:
    count = 0
    with open(in_file, "r") as fp:
        while line := fp.readline():
            with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json', 'r') as openfile:
                requirement_settings = json.load(openfile)

            words = line.strip().split(" ")
            
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

# don't mix coding styles (camelCase with snake_case ;) )
in_file = "D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\tellu.dsl"
parseDSL (in_file)
