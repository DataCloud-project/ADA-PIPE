from interface_json import PipelineDataContainer
from flask import Flask, render_template, Response, request, jsonify, make_response, redirect
import os
import json
import yaml
import socket
from waitress import serve
import keycloak_utils

DEBUG_MODE: bool = True
HOST_NUMBER: str = '0.0.0.0'
PORT_NUMBER: int = 5000

# Create a new Flask application
app = Flask(__name__)

FILE_PATH = '3ApplicationLogic.json'

with open('requirements.yaml', 'r') as file_read:
	requirement_list = json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))

with open('resources.json', 'r') as file_read:
	resource_list0 = json.load(file_read)
resource_list = json.dumps(resource_list0)

with open(FILE_PATH, 'r') as openfile:
    json_object = json.load(openfile)

data = json.dumps(json_object)
#pdc = PipelineDataContainer(FILE_PATH)

with open(FILE_PATH, 'r') as openfile:
    json_object = json.load(openfile)
data = json.dumps(json_object)

@app.route('/', methods=['GET', 'POST'])
def get_homepage():
    if request.method == 'POST':
        if request.form.get('action1') == 'INPUT1 - requirements':
            return redirect("/requirements", code=302) #Response(requirement_list, mimetype='text/yaml')
        elif  request.form.get('action2') == 'INPUT2 - resources':
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
	                if request.form.get('action1') == 'INPUT1 - requirements':
	                    return redirect("/requirements", code=302)
	                elif  request.form.get('action2') == 'INPUT2 - resources':
	                    return redirect("/resources", code=302) #Response(resource_list, mimetype='application/json')
	                else:
	                    return redirect("/schedules", code=302) #Response(data, mimetype='application/json')
    elif request.method == 'GET':
        #print(":D")
        return render_template("index.html", form=request.form)
    #print(":D:D")
    return render_template("index.html")

@app.route("/features", methods=['GET', 'POST'])
def index0():
    if request.method == "POST":
        return Response(file_file, mimetype='application/html' )

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
