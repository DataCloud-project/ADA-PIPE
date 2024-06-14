import subprocess
import json
with open('passwords.json', 'r') as openfile:
    passes = json.load(openfile)
def parseUserPipelines(requirement_settings,pipelineID):
        for i in range(len(requirement_settings["data"])):
                if (requirement_settings["data"][i]["id"]==pipelineID):
                        print(True)
                        return True
        print(pipelineID, " is not in the DEFinition PIPEline :'-(")
        return False
if __name__ == "__main__":
    user = "testuser"
    token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username="+user, "--data-urlencode", "password="+passes[user],
                   "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
    p = subprocess.Popen(token_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output, err = p.communicate()
    dict = json.loads(output.decode())
    user_token_ = dict["access_token"]
    #print(user_token_)

    def_repo_call = ["curl", "-X", "GET",
                "http://crowdserv.sys.kth.se:8082/api/repo/"+str(user),
                "-H", "accept: application/json"]
    p = subprocess.Popen(def_repo_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def_repo, err = p.communicate()
    dict = json.loads(output_of_def_repo.decode())
    #print(len(dict["data"]))
    #print(dict["data"])
    #print(dict["data"][len(dict["data"])-1]["id"])
    print(parseUserPipelines(dict,"3c51e0b0-bec4-49fd-be92-a88904fb8fef"))
    def_pipeline_call = ["curl", "-X", "GET",
                "http://crowdserv.sys.kth.se:8082/api/repo/export/"+str(user)+"/"+str(dict["data"][len(dict["data"])-1]["id"]),
                "-H", "accept: application/json"] #, "-H", "Authorization: Bearer {}".format(user_token_)]
    p = subprocess.Popen(def_pipeline_call, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    output_of_def_pipeline, err = p.communicate()
    dict = json.loads(output_of_def_pipeline.decode())
    #print(dict["data"])
