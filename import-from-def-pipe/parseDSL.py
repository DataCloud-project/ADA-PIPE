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
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME = words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "datacloud2.itec.aau.at/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "datacloud2.itec.aau.at/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "telluuser"
                elif (count == 1):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1-test1"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME = words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "datacloud2.itec.aau.at/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "datacloud2.itec.aau.at/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "telluuser"
                elif (count == 2):
                  requirement_settings["stepsList"][count]["provider"] = "DataCloud"
                  requirement_settings["stepsList"][count]["resource"] = "Datacloud-wp1-test2"
                  requirement_settings["stepsList"][count]["name"] = STEPS_NAME = words[3].lower().strip()
                  requirement_settings["stepsList"][count]["dockerImage"] = "datacloud2.itec.aau.at/"+STEPS_NAME+":latest"
                  requirement_settings["stepsList"][count]["dockerRegistry"] = "datacloud2.itec.aau.at/"
                  requirement_settings["stepsList"][count]["dockerUsername"] = "telluuser"
                  #requirement_settings["stepsList"][0]["dockerPassword"] = ""
                count += 1
            with open("TelluPipeline.json", "w") as outfile:
                json.dump(requirement_settings, outfile)

if __name__ == "__main__":
    with open('passwords.json', 'r') as openfile:
        passes = json.load(openfile)
    user = "user"
    token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username="+user, "--data-urlencode", "password="+passes[user],
                   "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
    p = subprocess.Popen(token_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output, err = p.communicate()
    dict = json.loads(output.decode())
    user_token_ = dict["access_token"]
    #                                                                                       
    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/d0bc11ef-2416-41fa-9357-ff0e2fbbdec4",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    print(dict["data"])
    parseDSLTellu(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/6a77d0fa-ae70-4372-9c44-08bb6fb1d7f6",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    print(dict["data"])
    #parseDSLBosch(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/e1536753-a88e-4489-85e4-84d555500e58",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    print(dict["data"])
    #parseDSLMog(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/468532e8-580e-4370-b246-352433cb76a7",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    print(dict["data"])
    #parseDSLJot(dict["data"])

    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/a6d3bea4-dc77-4a56-a086-4c6eab2ae4c4",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    print(dict["data"])
    #parseDSLCer(dict["data"])
