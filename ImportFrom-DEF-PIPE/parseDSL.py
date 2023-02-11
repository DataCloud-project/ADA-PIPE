import subprocess
import json
from parser_constants import *
import sys
sys.path.append('./parser_constants')


def parseDSL(in_file) -> None:
    count = 0
    with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json', 'r') as openfile:
        requirement_settings = json.load(openfile)
    for line in in_file.splitlines():
        words = line.split(' ')
        #print(words)
        STEPS_NAME =  "temp"
        if len(words) != 1:
            if (PIPELINE_NAME in words[0]):
                requirement_settings["pipelineName"] = str(words[1])
                requirement_settings["chunkName"] = words[1]+"UseCase"

            elif (words[0] == STEPS_REQ_MINCPU):
                requirement_settings["stepsList"][0]["requirement"]["vCPUs"] = ((float(words[1]))/1024.0)

            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][0]["requirement"]["ram"] = words[1]

            elif "data-processing step" in line or "data-source step" in line or "data-sink step" in line:
                requirement_settings["stepsList"][0]["name"] = STEPS_NAME = words[3].lower().strip()
                requirement_settings["stepsList"][0]["dockerImage"] = "datacloud2.itec.aau.at/"+STEPS_NAME+":latest"
                requirement_settings["stepsList"][0]["dockerRegistry"] = "datacloud2.itec.aau.at/"
                requirement_settings["stepsList"][0]["dockerUsername"] = "mogsport"
                #requirement_settings["stepsList"][0]["dockerPassword"] = ""

            #elif (words[0] == STEPS_IMPLEMENTATION):
            #    requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()

            #elif (words[0] == STEPS_REQ_MAXINS):
            #    requirement_settings = "???"

            if (count == 0):
                requirement_settings["stepsList"][0]["provider"] = "Tellu"
                requirement_settings["stepsList"][0]["resource"] = "Tellu Gateway 0"
            else:
                requirement_settings["stepsList"][0]["provider"] = "DataCloud"
                requirement_settings["stepsList"][0]["resource"] = "DatacloudWP1"
            with open("D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\"+STEPS_NAME+".json", "w") as outfile:
                json.dump(requirement_settings, outfile)
                count += 1


if __name__ == "__main__":
    token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded",
                  "--data-urlencode", "username=?????", "--data-urlencode", "password=??????", "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
    p = subprocess.Popen(token_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output, err = p.communicate()
    dict = json.loads(output.decode())
    user_token_ = dict["access_token"]
    def_call = ["curl", "-X", "GET", "https://crowdserv.sys.kth.se/api/repo/export/testuser/pipeline",
                "-H", "accept: application/json", "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def, err = p.communicate()
    dict = json.loads(output_of_def.decode())
    print(dict["data"])
    parseDSL(dict["data"])
