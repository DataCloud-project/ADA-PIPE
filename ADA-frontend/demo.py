from interface_json import PipelineDataContainer
from flask import Flask, render_template, Response, request, jsonify, make_response, redirect, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
import yaml
from waitress import serve
#import keycloak_utils
from flask_swagger_ui import get_swaggerui_blueprint
import subprocess
import hashlib
import collectMetrics
import pandas as pd

DEBUG_MODE: bool = True
HOST_NUMBER: str = '0.0.0.0'
PORT_NUMBER: int = 5000

# Create a new Flask application
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

requirement_list: list = list()
with open('requirements.yaml', 'r') as file_read:
    requirement_list = json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))

resource_list: list = list()
with open('resources.json', 'r') as file_read:
    resource_list0 = json.load(file_read)
    resource_list = json.dumps(resource_list0)

data: any = None
with open('data_analysis.json', 'r') as openfile:
    json_object = json.load(openfile)
    data = json_object #json.dumps(json_object)

mog_list: list = list()
with open('templates/mog.json', 'r') as file_read_mog:
    mog_list = json.load(file_read_mog)
    mog_list = json.dumps(mog_list)

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

@app.route("/pipelines", methods=['GET', 'POST'])
def index():
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
        if request.method == 'POST':
            if request.form.get('action1') == 'INPUT1 - requirements (template)':
                return redirect("/requirements", code=302)
            elif request.form.get('action2') == 'INPUT1 - requirements (from BC)':
                return redirect("/upload", code=302)
            elif request.form.get('action3') == 'INPUT2 - resources':
                return redirect("/resources", code=302)
            elif request.form.get('action4') == 'Schedules':
                return redirect("/schedules", code=302)
            else:
                return redirect("/swagger", code=302)
    elif request.method == 'GET':
        #print(":D")
        return render_template("./index.html", form=request.form)
    #print(":D:D")
    return render_template("./index.html")

@app.route('/upload')
def upload_page():
    '''if request.form.get('Download') == 'Download - requirements (template)':
            return redirect("/download", code=302) #Response(requirement_list, mimetype='text/yaml')
    else:'''
    return render_template('./upload.html')

@app.route('/download', methods=['GET'])
def downloadFile ():
    path = "requirements-temp.json"
    return (send_file(path,  mimetype='application/json' ,as_attachment=True) and redirect("/upload", code=302))

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GAET':
        downloadFile ()
    elif request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join('uploaded', filename))
      return ('file uploaded successfully' and redirect("/", code=302))

@app.route("/importData",  methods=['GET'])
def importData():
     #data_call = ["curl","http://localhost:19999/api/v1/allmetrics?format=prometheus&help=yes"]
     #p = subprocess.Popen(data_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     #output, err = p.communicate()
     #return (output.decode())
     #return render_template("simple.html", tables=[collectMetrics.prepared_dataframe.to_html(classes='data')], titles=collectMetrics.prepared_dataframe.columns.values)
     return collectMetrics.prepared_dataframe.to_html(header="true", table_id="table")

@app.route("/adaptExecution/<string:pipeline>/<string:chunk>", methods=['GET'])
def adaptExecution(pipeline,chunk):
    try:
        if (os.path.exists(chunk+".json")):
                with open(chunk+'.json', 'r') as openfile:
                        json_object = json.load(openfile)
                        if(json_object["pipelineName"] == str(pipeline)):
                            return ('Successfully loaded' and Response(json.dumps(json_object), mimetype='application/json' ))
        else:
                #data["pipelineName"] = str(pipeline)
                #data["stepsList"][0]["name"] = str(chunk)
                #return  ('The requested pipeline or chunk is not available' and Response(json.dumps(data), mimetype='application/json' ))
                return Response("<p>Please test again with the pipeline name of pipeline and chunk name of what-if_analysis</p>", mimetype='text/html') #('The requested pipeline or chunk is not available' and Response(json.dumps(data), mimetype='application/json' ))
    except FileNotFoundError:
        return

@app.route("/predict", methods=['GET'])
def predict():
     return "<p>DatacloudWP1</p>" #ml.predict()

@app.route("/import_pipeline", methods=['GET'])
def import_pipeline():
    user: str = 'testuser'
    pipeline: str = 'pipeline'
    try:
        return (redirect(f"/importPipeline/{user}/{pipeline}", code=302))
    except FileNotFoundError:
        return

@app.route("/importPipeline/<string:user>/<string:pipeline>", methods=['POST', 'GET'])
def importPipeline(user,pipeline):
    #if request.method == "POST":
    try:
        token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username=?????", "--data-urlencode", "password=?????", "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
        p = subprocess.Popen(token_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        dict = json.loads(output.decode())
        user_token_ = dict["access_token"]
        def_call = ["curl", "-X", "GET","https://crowdserv.sys.kth.se/api/repo/export/testuser/pipeline", "-H","accept: application/json","-H","Authorization: Bearer {}".format(user_token_)]
        p = subprocess.Popen(def_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_of_def, err = p.communicate()
        dict = json.loads(output_of_def.decode())
        return Response(dict["data"], mimetype='application/json' )

    except FileNotFoundError:
        #print(":D")
        return

@app.route("/importUser/<string:user>", methods=['POST','GET'])
def importUser(user):
    try:
        token_call = ["curl", "--location", "--request", "POST", "https://datacloud-auth.euprojects.net/auth/realms/user-authentication/protocol/openid-connect/token", "--header", "Content-Type: application/x-www-form-urlencoded", "--data-urlencode", "username=?????", "--data-urlencode", "password=?????", "--data-urlencode", "realm=user-authentication", "--data-urlencode", "client_id=def_frontend", "--data-urlencode", "grant_type=password"]
        p = subprocess.Popen(token_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        dict = json.loads(output.decode())
        user_token_ = dict["access_token"]
        h = hashlib.sha256()
        h.update(str(dict["access_token"]).encode(encoding='UTF-8'))
        return h.hexdigest()
    except FileNotFoundError:
        return

@app.route("/importRuntimeMetrics", methods=['POST', 'GET'])
def importRuntimeMetrics():
    try:
        #collectMetrics.prepared_dataframe
        #return ('Loaded successfully' and redirect("/resources", code=302))
        #return render_template("simple.html",  tables=[collectMetrics.prepared_dataframe.to_html(classes='data')], titles=collectMetrics.prepared_dataframe.columns.values)
        #if ("cpu" in runtime_metrics):
        #      return collectMetrics.prepared_dataframe["cpu.cpu3"].to_html(header="true", table_id="table")
        #elif ("mem" in runtime_metrics):
        #      return collectMetrics.prepared_dataframe["services.mem_usage"].to_html(header="true", table_id="table")
        #else:
        return collectMetrics.prepared_dataframe.to_html(header="true", table_id="table")
    except FileNotFoundError:
        return

@app.route("/import_mog_pipeline", methods=['GET'])
def import_mog_pipeline():
    try:
         #return Response (json.load(open('templates/mog.dsl', 'r').decode()), mimetype='application/json')
         #cat_call = ["cat", "./mog.dsl"]
         #p = subprocess.Popen(cat_call, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         #output, err = p.communicate()
         #dictdict = json.loads(output.decode())
         #return  Response(dictdict, mimetype='application/json')
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
