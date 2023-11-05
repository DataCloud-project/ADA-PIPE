from flask import Flask, render_template, Response, request, jsonify, make_response, redirect, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
import yaml
from waitress import serve
import keycloak_utils
from flask_swagger_ui import get_swaggerui_blueprint
import subprocess
import hashlib
#import collectMetrics
#import predict_func
#import detect_anomaly
import pandas as pd

DEBUG_MODE: bool = True
HOST_NUMBER: str = '0.0.0.0'
PORT_NUMBER: int = 5000

# Create a new Flask application
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
with open('requirements.yaml', 'r') as file_read:
        requirement_list = json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))
with open('dry-run.yaml', 'r') as file_read:
        dry_run_list = json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))
with open('resources.json', 'r') as file_read:
        resource_list0 = json.load(file_read)
resource_list = json.dumps(resource_list0)

with open('passwords.json', 'r') as openfile:
    passes = json.load(openfile)

with open('TelluPipeline.json', 'r') as openfile:
    json_object = json.load(openfile)
data = json_object #json.dumps(json_object)
with open('templates/mog.json', 'r') as file_read_mog:
    mog_list = json.load(file_read_mog)
mog_list = json.dumps(mog_list)

with open("data0.txt", "r") as fp:
    cont_step_image = fp.readlines()
with open("data1.txt", "r") as fp:
    cont_device = fp.readlines()
with open("data2.txt", "r") as fp:
    cont_sched = fp.readlines()
user_token_ = 0

# flask swagger configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# error handeling
@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

@app.route('/', methods=['GET', 'POST'])
def get_homepage():
    if request.method == 'POST':
        if request.form.get('action1') == 'Requirements (template)':
            return redirect("/requirements", code=302)
        elif request.form.get('action2') == 'Requirements':
            return redirect("/upload", code=302)
        elif  request.form.get('action3') == 'WorkerPools':
            return redirect("/resources", code=302)
        elif request.form.get('action4') == 'Schedules':
            return redirect("/schedules", code=302)
        else:
            return redirect("/swagger", code=302)
    elif request.method == 'GET':
        return render_template("index.html", form=request.form)
    return render_template("index.html")

'''@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        # Get Form Fields
        ##username = input("Please enter username: ")  #request.form['username']
        #password_candidate = input("Please enter password: ")  #request.form['password']
        #print(username, " ",password_candidate)
        #keycloak_open_id = keycloak_utils._get_keycloak_open_id()
        #keycloak_token = keycloak_utils._get_keycloak_token(username,password_candidate)
        #access_token = keycloak_token['access_token']
        #print(access_token)
        #user_info = keycloak_utils.verify_access_token(access_token)
        #print("Token is verified :D :D ",user_info)
        #if(user_info == True):
        if request.method == 'GET':
           return render_template("./index.html", form=request.form)
        return render_template("./index.html")'''

@app.route('/upload')
def upload_page():
    return render_template('./upload.html')

@app.route('/download', methods=['GET'])
def downloadFile ():
    path = "requirements-temp.json"
    return (send_file(path,  mimetype='application/json' ,as_attachment=True) and redirect("/upload", code=302))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        downloadFile ()
    elif request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join('uploaded', filename))
      return ('file uploaded successfully' and redirect("/", code=302))

@app.route("/importData",  methods=['GET'])
def importData():
     #return render_template("simple.html", tables=[collectMetrics.prepared_dataframe.to_html(classes='data')], titles=collectMetrics.prepared_dataframe.columns.values)
     return #collectMetrics.prepared_dataframe.to_html(header="true", table_id="table")

def parseUserPipelines(requirement_settings,pipelineID):
	for i in range(len(requirement_settings["data"])):
		if (requirement_settings["data"][i]["id"]==pipelineID):
			return True
	return False
	#print(len(requirement_settings["data"]))

@app.route("/adaptExecution/<string:user>/<string:pipelineID>", methods=['POST', 'GET'])
def adaptExecution(user,pipelineID):
            try:
                token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username="+user, "--data-urlencode", "password="+passes[user], "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
                p = subprocess.Popen(token_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = p.communicate()
                dict = json.loads(output.decode())
                user_token_ = dict["access_token"]
                def_call = ["curl", "-X", "GET","https://crowdserv.sys.kth.se/api/repo/"+user, "-H","accept: application/json","-H","Authorization: Bearer {}".format(user_token_)]
                p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                output_of_def, err = p.communicate()
                dict = json.loads(output_of_def.decode())
                if (parseUserPipelines(dict,pipelineID)):
                        if (os.path.exists(pipelineID+".json")):
                                with open(pipelineID+'.json', 'r') as openfile:
                                    json_object = json.load(openfile)
                                    return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json' ))
                        else:
                                #os.path.join(pipelineID+".json")
                                if ("bosch" in user):
                                    with open('6a77d0fa-ae70-4372-9c44-08bb6fb1d7f6.json', 'r') as openfile:
                                        json_object = json.load(openfile)
                                        return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json'))
                                        #os.popen('cp '+' '+'6a77d0fa-ae70-4372-9c44-08bb6fb1d7f6.json'+' '+pipelineID+".json")
                                elif("tlu" in user):
       	                            with open('d0bc11ef-2416-41fa-9357-ff0e2fbbdec4.json', 'r') as openfile:
                                        json_object = json.load(openfile)
                                        return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json')) #os.popen('cp '+' '+'d0bc11ef-2416-41fa-9357-ff0e2fbbdec4.json'+' '+pipelineID+".json")
                                elif("jot" in user):
                                    with open('468532e8-580e-4370-b246-352433cb76a7.json', 'r') as openfile:
                                        json_object = json.load(openfile)
                                        return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json'))
                                        #os.popen('cp '+' '+'468532e8-580e-4370-b246-352433cb76a7.json'+' '+pipelineID+".json")
                                elif("mog" in user):
                                    with open('e1536753-a88e-4489-85e4-84d555500e58.json', 'r') as openfile:
                                        json_object = json.load(openfile)
                                        return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json'))
                                        #os.popen('cp '+' '+'e1536753-a88e-4489-85e4-84d555500e58.json'+' '+pipelineID+".json")
                                elif("cer" in user):
                                    with open('a6d3bea4-dc77-4a56-a086-4c6eab2ae4c4.json', 'r') as openfile:
                                        json_object = json.load(openfile)
                                        return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json'))
                                        #os.popen('cp '+' '+'a6d3bea4-dc77-4a56-a086-4c6eab2ae4c4.json'+' '+pipelineID+".json")
                else:
                        with open('37382275-2196-47c3-8d06-d21a30c91392.json', 'r') as openfile:
                              json_object = json.load(openfile)
                        return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json'))
                	        #os.popen('cp '+' '+'37382275-2196-47c3-8d06-d21a30c91392.json'+' '+pipelineID+".json")
        	                #with open(pipelineID+".json", 'r') as openfile:
	                        #     json_object = json.load(openfile)
	                        #     return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json'))
	                        #return Response("<p>Please test again with the PipelineID</p>", mimetype='text/html') #('The requested pipeline or chunk is not available' and Response(json.dumps(data), mimetype='application/json' ))
            except FileNotFoundError:
                return

@app.route("/alloc", methods=['GET'])
def alloc():
     return render_template("prediction.html")

@app.route("/alloc/sched", methods=['GET', 'POST'])
def alloc2():
        if request.form.get('action1') == 'Import Docker images of steps':
            return render_template("prediction0.html", header= "Loading Docker images of steps from repo",len = 22, cont = cont_step_image)
        elif request.form.get('action2') == 'Import device descriptions':
            return render_template("prediction0.html", header="Getting devices monitoring information", len = 2, cont = cont_device)
        elif  request.form.get('action3') == 'Schedule':
            return render_template("tellu.html")

@app.route("/predict", methods=['GET'])
def predict():
            try:
                return ###predict_func.prepared_dataframe.to_html(header="true", table_id="table")
            except FileNotFoundError:
                return

@app.route("/detectAnomaly", methods=['GET'])
def detectAnomaly():
            try:
                return ###detect_anomaly.prepared_dataframe.to_html(header="true", table_id="table")
            except FileNotFoundError:
                return

@app.route("/import_demo_pipeline", methods=['GET'])
def import_demo_pipeline():
            try:
                return (redirect("/importPipeline/{}/{}".format("testuser","8006f770-4315-4d87-a0b9-7dd5f1c8f2d7"), code=302))
            except FileNotFoundError:
                return

@app.route("/import_tel_pipeline", methods=['GET'])
def import_tel_pipeline():
            try:
                #return(redirect("/importPipeline/{}/{}".format("testuser","37382275-2196-47c3-8d06-d21a30c91392"), code=302))
                #return(redirect("/importPipeline/{}/{}".format("testuser","29b85ff2-fd0c-4499-8764-e411fc066033"), code=302))
                return(redirect("/importPipeline/{}/{}".format("testuser","d0bc11ef-2416-41fa-9357-ff0e2fbbdec4"), code=302))
                #return(redirect("/importPipeline/{}/{}".format("testuser","028c9ef7-58cb-438a-b7a9-71e7511a3ddc"), code=302))
            except FileNotFoundError:
                return
@app.route("/import_mog_pipeline", methods=['GET'])
def import_mog_pipeline():
            try:
                #return(redirect("/importPipeline/{}/{}".format("testuser","f4db3cdb-9cb7-417c-8266-fda2f82f400e"), code=302))
                #return(redirect("/importPipeline/{}/{}".format("testuser","514d20db-2bf4-417f-a31b-196d53e72baa"), code=302))
                return(redirect("/importPipeline/{}/{}".format("testuser","e1536753-a88e-4489-85e4-84d555500e58"), code=302))
            except FileNotFoundError:
                return
@app.route("/import_jot_pipeline", methods=['GET'])
def import_jot_pipeline():
            try:
                return (redirect("/importPipeline/{}/{}".format("testuser","468532e8-580e-4370-b246-352433cb76a7"), code=302))
            except FileNotFoundError:
                return
@app.route("/import_cer_pipeline", methods=['GET'])
def import_cer_pipeline():
            try:
                return (redirect("/importPipeline/{}/{}".format("testuser","a6d3bea4-dc77-4a56-a086-4c6eab2ae4c4"), code=302))
            except FileNotFoundError:
                return
@app.route("/import_bos_pipeline", methods=['GET'])
def import_bos_pipeline():
            try:
                return (redirect("/importPipeline/{}/{}".format("testuser","6a77d0fa-ae70-4372-9c44-08bb6fb1d7f6"), code=302)) 
                #"03b6755d-348d-47a5-9f5b-593659ad48ef"), code=302))
                #"5f642f50-4722-4d02-8e16-ee009fe08cc9"), code=302))
                #return (redirect("/importPipeline/{}/{}".format("testuser","8f155bc0-f5bb-42ce-b8dc-fafca0b7051c"), code=302))
                #return (redirect("/importPipeline/{}/{}".format("testuser","f0dd40df-9de7-4f51-b9b6-5327c587157d"), code=302))
            except FileNotFoundError:
                return
@app.route("/importPipeline/<string:user>/<string:pipelineID>", methods=['POST', 'GET'])
def importPipeline(user,pipelineID):
            try:
                token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username="+user, "--data-urlencode", "password="+passes[user], "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
                p = subprocess.Popen(token_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = p.communicate()
                dict = json.loads(output.decode())
                user_token_ = dict["access_token"]
                def_call = ["curl", "-X", "GET","https://crowdserv.sys.kth.se/api/repo/export/"+user+"/"+pipelineID, "-H","accept: application/json","-H","Authorization: Bearer {}".format(user_token_)]
                p = subprocess.Popen(def_call, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                output_of_def, err = p.communicate()
                dict = json.loads(output_of_def.decode())
                print(dict["data"])
                return Response((dict["data"]), mimetype='application/json' )
            except FileNotFoundError:
                return
@app.route("/importSimData/<string:user>/<string:pipelineID>", methods=['POST','GET'])
def importSimData(user,pipelineID):
            try:
                return Response(dry_run_list, mimetype='text/yaml')
            except FileNotFoundError:
                return

@app.route("/importUser/<string:user>", methods=['POST','GET'])
def importUser(user):
    try:
        token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username="+user, "--data-urlencode", "password="+passes[user], "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
        p = subprocess.Popen(token_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        dict = json.loads(output.decode())
        user_token_ = dict["access_token"]
        #access_token = keycloak_token['access_token']
        #print(access_token)
        user_info = keycloak_utils.verify_access_token(user_token_)
        if(user_info == True):
           print("Token is verified :D :D ",user_info)
           h = hashlib.sha256()
           h.update(str(dict["access_token"]).encode(encoding='UTF-8'))
           return "<p>User is verified: {} </p>".format(h.hexdigest())
    except FileNotFoundError:
        return

@app.route("/importRuntimeMetrics", methods=['POST', 'GET'])
def importRuntimeMetrics():
            try:
                #if ("cpu" in runtime_metrics):
                #      return collectMetrics.prepared_dataframe["cpu.cpu3"].to_html(header="true", table_id="table")
                #elif ("mem" in runtime_metrics):
                #      return collectMetrics.prepared_dataframe["services.mem_usage"].to_html(header="true", table_id="table")
                return ####collectMetrics.prepared_dataframe.to_html(header="true", table_id="table")
            except FileNotFoundError:
                return

@app.route("/import_mog_pipeline_demo", methods=['GET'])
def import_mog_pipeline_demo():
    try:
         return Response((mog_list), mimetype='application/json')
    except FileNotFoundError:
         return

@app.route("/matchMOG", methods=['GET'])
def matchMOG():
    try:
        return render_template('./mog.html')
    except FileNotFoundError:
        return
@app.route("/requirements", methods=['GET'])
def index1():
    if request.method == 'GET':
        return Response(requirement_list, mimetype='text/yaml')

@app.route("/resources", methods=['GET'])
def index2():
    if request.method == 'GET':
        return Response(resource_list, mimetype='application/json')

@app.route("/schedules", methods=['GET'])
def index3():
    if request.method == 'GET':
        return Response(data, mimetype='application/json')

if __name__ == '__main__':

    if DEBUG_MODE:
        # debug mode
        app.run(host=HOST_NUMBER, port=PORT_NUMBER, debug=True)
    else:
        # production mode
        host_name = socket.gethostname()
        IP_address = socket.gethostbyname(host_name)
        print(f'Running on http://{IP_address}/{PORT_NUMBER}/ (Press CTRL+C to quit)')
        serve(app, host=HOST_NUMBER, port=PORT_NUMBER)
