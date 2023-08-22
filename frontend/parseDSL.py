import subprocess
import json
from parser_constants import *
#import sys
#sys.path.append('./parser_constants')


def parseDSLTellu(in_file) -> None:
    count = 0
    with open('3ApplicationLogic.json', 'r') as openfile:
        requirement_settings = json.load(openfile)
    for line in in_file.splitlines():
        words = line.split(' ')
        #print(words)
        STEPS_NAME =  "temp"
        if len(words) != 1:
            if (PIPELINE_NAME in words[0]):
                requirement_settings["pipelineName"] = str("TelluPipeline")
                requirement_settings["chunkName"] = "Tellu"+"UseCase"
            elif (words[0] == STEPS_REQ_MINCPU):
                requirement_settings["stepsList"][count]["requirement"]["vCPUs"] = ((float(words[1]))/1024.0)
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][count]["requirement"]["ram"] = words[1]
            elif "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                #print(count)
                if (count == 0):
                  requirement_settings["stepsList"][count]["provider"] = "Tellu"
                  requirement_settings["stepsList"][count]["resource"] = "Tellu Gateway 0"
                  STEPS_NAME = "dcgenerate"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  #requirement_settings["stepsList"][count]["dockerUsername"] = "telluuser"
                elif (count == 1):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1-test1"
                  STEPS_NAME = "dcreceive"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  #requirement_settings["stepsList"][count]["dockerUsername"] = "telluuser"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1-test2"
                  STEPS_NAME = "dcnotification"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  #requirement_settings["stepsList"][count]["dockerUsername"] = "telluuser"
                  #requirement_settings["stepsList"][0]["dockerPassword"] = ""
                count += 1

            #elif (words[0] == STEPS_IMPLEMENTATION):
            #    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
            #elif (words[0] == STEPS_REQ_MAXINS):
            #    requirement_settings = "???"

            with open("37382275-2196-47c3-8d06-d21a30c91392.json", "w") as outfile:
                json.dump(requirement_settings, outfile)
                #count += 1
def parseDSLBosch(in_file) -> None:
    count = 0
    with open('boschLogic.json', 'r') as openfile:
        requirement_settings = json.load(openfile)
    for line in in_file.splitlines():
        words = line.split(' ')
        #print(words)
        STEPS_NAME =  "temp"
        if len(words) != 1:
            if (PIPELINE_NAME in words[0]):
                requirement_settings["pipelineName"] = str("BoschPipeline")
                requirement_settings["chunkName"] = "Bosch"+"UseCase"
            elif (words[0] == STEPS_REQ_MINCPU):
                requirement_settings["stepsList"][count]["requirement"]["vCPUs"] = ((float(words[1]))/1024.0)
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][count]["requirement"]["ram"] = words[1]
            elif "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                #print(count)
                if (count == 0):
                  requirement_settings["stepsList"][count]["provider"] = "Bosch"
                  requirement_settings["stepsList"][count]["resource"] = "Bosch Gateway 0"
                  STEPS_NAME = "dataretrieve"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "boschapi"
                elif (count == 1):
                  requirement_settings["stepsList"][count]["provider"] = "Bosch"
                  requirement_settings["stepsList"][count]["resource"] = "Bosch Gateway 1"
                  STEPS_NAME = "dataslice"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "boschapi"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1"
                  STEPS_NAME = "dataprepare"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "boschapi"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp2"
                  STEPS_NAME = "datastore"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "boschapi"
                  #requirement_settings["stepsList"][0]["dockerPassword"] = ""
                count += 1

            #elif (words[0] == STEPS_IMPLEMENTATION):
            #    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
            #elif (words[0] == STEPS_REQ_MAXINS):
            #    requirement_settings = "???"

            with open("5f642f50-4722-4d02-8e16-ee009fe08cc9.json", "w") as outfile:
                json.dump(requirement_settings, outfile)
def parseDSLMog(in_file) -> None:
    count = 0
    with open('mogLogic.json', 'r') as openfile:
    #with open('mogLogic-withbroker.json', 'r') as openfile:
        requirement_settings = json.load(openfile)
    for line in in_file.splitlines():
        words = line.split(' ')
        #print(words)
        STEPS_NAME =  "temp"
        if len(words) != 1:
            if (PIPELINE_NAME in words[0]):
                requirement_settings["pipelineName"] = str("MogPipeline")
                requirement_settings["chunkName"] = "Mog"+"UseCase"
            elif (words[0] == STEPS_REQ_MINCPU):
                requirement_settings["stepsList"][count]["requirement"]["vCPUs"] = ((float(words[1]))/1024.0)
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][count]["requirement"]["ram"] = words[1]
            elif "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                #print(count)
                if (count == 0):
                  requirement_settings["stepsList"][count]["provider"] = "Mog"
                  requirement_settings["stepsList"][count]["resource"] = "DataCloud-edge-0"
                  STEPS_NAME = "detection_right"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/detection:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "mogapi"
                elif (count == 1):
                  requirement_settings["stepsList"][count]["provider"] = "Mog"
                  requirement_settings["stepsList"][count]["resource"] = "DataCloud-edge-0"
                  STEPS_NAME = "detection_left"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/detection:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "mogapi"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1"
                  STEPS_NAME = "fusion"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "mogapi"
                elif (count == 3):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1"
                  STEPS_NAME = "overlay"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "mogapi"
                  #requirement_settings["stepsList"][0]["dockerPassword"] = ""
                count += 1

            #elif (words[0] == STEPS_IMPLEMENTATION):
            #    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
            #elif (words[0] == STEPS_REQ_MAXINS):
            #    requirement_settings = "???"

            with open("f4db3cdb-9cb7-417c-8266-fda2f82f400e.json", "w") as outfile:
                json.dump(requirement_settings, outfile)

def parseDSLJot(in_file) -> None:
    count = 0
    with open('jotLogic.json', 'r') as openfile:
        requirement_settings = json.load(openfile)
    for line in in_file.splitlines():
        words = line.split(' ')
        #print(words)
        STEPS_NAME =  "temp"
        if len(words) != 1:
            if (PIPELINE_NAME in words[0]):
                requirement_settings["pipelineName"] = str("JotPipeline")
                requirement_settings["chunkName"] = str("JotUseCase")
                requirement_settings["pipelineType"] = str("batch")
            elif (words[0] == STEPS_REQ_MINCPU):
                requirement_settings["stepsList"][count]["requirement"]["vCPUs"] = ((float(words[1]))/1024.0)
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][count]["requirement"]["ram"] = words[1]
            elif "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                #print(count)
                if (count == 0):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "DataCloud-wp1"
                  STEPS_NAME = "DataCleaning_Conv"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/conversions_img:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "jotapi"
                elif (count == 1):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1"
                  STEPS_NAME = "DataCleaning_Stats"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/statistics_img:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "jotapi"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1"
                  STEPS_NAME = "DataCleaning_Rev"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/revenue_img:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "jotapi"
                  #requirement_settings["stepsList"][0]["dockerPassword"] = ""
                count += 1

            #elif (words[0] == STEPS_IMPLEMENTATION):
            #    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
            #elif (words[0] == STEPS_REQ_MAXINS):
            #    requirement_settings = "???"

            with open("468532e8-580e-4370-b246-352433cb76a7.json", "w") as outfile:
                json.dump(requirement_settings, outfile)

def parseDSLCer(in_file) -> None:
    count = 0
    with open('ceramicaLogic.json', 'r') as openfile:
        requirement_settings = json.load(openfile)
    for line in in_file.splitlines():
        words = line.split(' ')
        #print(words)
        STEPS_NAME =  "temp"
        if len(words) != 1:
            if (PIPELINE_NAME in words[0]):
                requirement_settings["pipelineName"] = str("CerPipeline")
                requirement_settings["chunkName"] = str("CerUseCase")
            elif (words[0] == STEPS_REQ_MINCPU):
                requirement_settings["stepsList"][count]["requirement"]["vCPUs"] = ((float(words[1]))/1024.0)
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][count]["requirement"]["ram"] = words[1]
            elif "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                #print(count)
                if (count == 0):
                  requirement_settings["stepsList"][count]["provider"] = "Cer"
                  requirement_settings["stepsList"][count]["resource"] = "DataCloud-edge-0"
                  STEPS_NAME = "Data_Analysis"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME  #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/data-analysis:heavy"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "cerapi"
                elif (count == 1):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1"
                  STEPS_NAME = "Digital_Twins"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/simulation:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "cerapi"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "Cer"
                  requirement_settings["stepsList"][count]["resource"] = "DataCloud-edge-1"
                  STEPS_NAME = "What-If_Analysis"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME #= words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "dcloud2.itec.aau.at:5000/what-if-analysis:latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "dcloud2.itec.aau.at:5000/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "cerapi"
                  #requirement_settings["stepsList"][0]["dockerPassword"] = ""
                count += 1

            #elif (words[0] == STEPS_IMPLEMENTATION):
            #    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
            #elif (words[0] == STEPS_REQ_MAXINS):
            #    requirement_settings = "???"

            with open("a6d3bea4-dc77-4a56-a086-4c6eab2ae4c4.json", "w") as outfile:
                json.dump(requirement_settings, outfile)

if __name__ == "__main__":
    token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded",
                  "--data-urlencode", "username=testuser", "--data-urlencode", "password=?????", "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
    p = subprocess.Popen(token_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output, err = p.communicate()
    dict = json.loads(output.decode())
    user_token_ = dict["access_token"]
    #                                                                                       37382275-2196-47c3-8d06-d21a30c91392
    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/37382275-2196-47c3-8d06-d21a30c91392",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    #print(dict["data"])
    parseDSLTellu(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/5f642f50-4722-4d02-8e16-ee009fe08cc9",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    #print(dict["data"])
    parseDSLBosch(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/f4db3cdb-9cb7-417c-8266-fda2f82f400e",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    #print(dict["data"])
    parseDSLMog(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/468532e8-580e-4370-b246-352433cb76a7",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    #print(dict["data"])
    parseDSLJot(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/a6d3bea4-dc77-4a56-a086-4c6eab2ae4c4",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    #print(dict["data"])
    parseDSLCer(dict["data"])
