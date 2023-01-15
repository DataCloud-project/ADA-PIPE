from interface_json import PipelineDataContainer
from flask import Flask, render_template, Response, request, jsonify, make_response, redirect
from werkzeug.utils import secure_filename
import os
import json
import yaml
import socket
from waitress import serve
import keycloak_utils
from flask_swagger_ui import get_swaggerui_blueprint

DEBUG_MODE: bool = True
HOST_NUMBER: str = '0.0.0.0'
PORT_NUMBER: int = 5000

# Create a new Flask application
app = Flask(__name__)

with open('requirements.yaml', 'r') as file_read:
	requirement_list = json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))

with open('resources.json', 'r') as file_read:
	resource_list0 = json.load(file_read)
resource_list = json.dumps(resource_list0)

'''with open('D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\3ApplicationLogic.json', 'r') as openfile:
    json_object = json.load(openfile)
data = json.dumps(json_object)
#pdc = PipelineDataContainer(FILE_PATH)'''

with open('3ApplicationLogic.json', 'r') as openfile:
    json_object = json.load(openfile)
data = json.dumps(json_object)

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
        if request.form.get('action1') == 'INPUT1 - requirements (template)':
            return redirect("/requirements", code=302) #Response(requirement_list, mimetype='text/yaml')
        elif request.form.get('action2') == 'INPUT1 - requirements (from BC)':
            return redirect("/upload", code=302)
        elif  request.form.get('action3') == 'INPUT2 - resources':
            return redirect("/resources", code=302) #Response(resource_list, mimetype='application/json')
        else:
            return redirect("/schedules", code=302) #Response(data, mimetype='application/json')
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
                return redirect("/requirements", code=302) #Response(requirement_list, mimetype='text/yaml')
            elif request.form.get('action2') == 'INPUT1 - requirements (from BC)':
                return redirect("/upload", code=302)
            elif request.form.get('action3') == 'INPUT2 - resources':
                return redirect("/resources", code=302) #Response(resource_list, mimetype='application/json')
            else:
                return redirect("/schedules", code=302) #Response(data, mimetype='application/json')
    elif request.method == 'GET':
        #print(":D")
        return render_template("./index.html", form=request.form)
    #print(":D:D")
    return render_template("./index.html")

@app.route('/upload')
def upload_page():
   return render_template('./upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join('./uploaded/', filename))
      return ('file uploaded successfully' and redirect("/", code=302))

'''@app.route("/features", methods=['GET', 'POST'])
def index0():
    if request.method == "POST":
        return Response(file_file, mimetype='application/html' )
'''
@app.route("/adaptExecution/<int:pipelineID>/<int:runtime_metrics>", methods=['GET'])
def index0(pipelineID,runtime_metrics):
    #if request.method == "POST":
            try:
                # pipelineID = data[pipelineID]
                # runtime_metrics = data[runtime_metrics]
                # data = {
                #         "pipelineID": pipelineID,
                #         "runtime_metrics": runtime_metrics,
                #         "timestamp": get_timestamp(),
                #     }
                return Response(data, mimetype='application/json')

            except FileNotFoundError:
                return

@app.route("/importPipeline/<string:pipelineID>", methods=['POST'])
def importPipeline(pipelineID):
    #if request.method == "GET":
            try:
                # pipelineID = data[pipelineID]
                # runtime_metrics = data[runtime_metrics]
                # data = {
                #         "pipelineID": pipelineID,
                #         "runtime_metrics": runtime_metrics,
                #         "timestamp": get_timestamp(),
                #     }
                return ('Received successfully' and redirect("/requirements", code=302))

            except FileNotFoundError:
                return
@app.route("/importWorkerPools/<string:workerPools>", methods=['POST'])
def importWorkerPools(workerPools):
    #if request.method == "GET":
            try:
                # pipelineID = data[pipelineID]
                # runtime_metrics = data[runtime_metrics]
                # data = {
                #         "pipelineID": pipelineID,
                #         "runtime_metrics": runtime_metrics,
                #         "timestamp": get_timestamp(),
                #     }
                return ('Received successfully') # and redirect("/resources", code=302))

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

