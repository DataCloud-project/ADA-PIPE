import sys
sys.path.append('./parser_constants')
from parser_constants import *
import json
import subprocess

def parseDSL (in_file) -> None:
    count = 0
    for line in in_file.splitlines():    
            with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json', 'r') as openfile:
                requirement_settings = json.load(openfile)
            #print(line)
            words = line.split(' ')
            #print(words)
            if  len(words) != 1:
                #print(words[0])
                if (PIPELINE_NAME in words[0]):
                    #print(requirement_settings["pipelineName"])
                    requirement_settings["pipelineName"]= words[1]+"_pipeline"
                elif (words[0] == STEPS_REQ_MINCPU):
                    #print(words[1])
                    requirement_settings["stepsList"][0]["requirement"]["vCPUs"]=((float(words[1]))/1024.0)
                    
                elif (words[0] == STEPS_REQ_MINMEM):
                    requirement_settings["stepsList"][0]["requirement"]["ram"] = words[1]
                    
                elif (words[0] == STEPS_IMPLEMENTATION):
                    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
                
                elif (words[0] == STEPS_REQ_MAXINS):
                    requirement_settings  = requirement_settings  #?????
                    
    
            if (count == 0):
                requirement_settings["stepsList"][0]["provider"] = "Tellu" 
                requirement_settings["stepsList"][0]["resource"] = "Tellu Gateway 0" 
            else:
                requirement_settings["stepsList"][0]["provider"] = "DataCloud-k8s"
                requirement_settings["stepsList"][0]["resource"] = "DataCloud-k8s-1"
            #print("data-processing step" in line)   
            if "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                count += 1
                #print(count)
                #if "data-processing step" in line:
                requirement_settings["stepsList"][0]["name"] = STEPS_NAME = words[3].lower().strip()
                #print((words[3].lower().strip()))
                with open("D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\"+STEPS_NAME+".json", "w") as outfile:
                    json.dump(requirement_settings,outfile)
    #print()


token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username=?????", "--data-urlencode", "password=??????", "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
p = subprocess.Popen(token_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate()
dict = json.loads(output.decode())
user_token_ = dict["access_token"]
def_call = ["curl", "-X", "GET","https://crowdserv.sys.kth.se/api/repo/export/testuser/pipeline", "-H","accept: application/json","-H","Authorization: Bearer {}".format(user_token_)]
p = subprocess.Popen(def_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output_of_def, err = p.communicate()
dict = json.loads(output_of_def.decode())
print(dict["data"])
parseDSL (dict["data"])
