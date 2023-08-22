#!/usr/bin/env python3

# source: https://towardsdatascience.com/a-python-api-for-background-requests-based-on-flask-and-multi-processing-187d0e3049c9
from flask import Flask, abort, jsonify, render_template, Response, request
from waitress import serve
from flask_cors import CORS


import json

from interface_json import PipelineDataContainer
from pipeline_state import PipelineState

DEBUG_MODE: bool = True
HOST_NUMBER: str = '0.0.0.0'
PORT_NUMBER: int = 5000

pipeline_state: PipelineState = PipelineState(add_dummy_data=True)

REST_GET: str = 'GET'
REST_POST: str = 'POST'

# Create a new Flask application
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=[REST_GET])
def get_homepage():
    text = 'Hello World'
    return render_template('index.html', html_page_text=text)


# TODO
# @app.route('/jobs', methods=[REST_GET])
# def get_jobs():
#     jobs = {'job': [job._job_dict for job in pdc.get_jobs()]}
#     return Response(json.dumps(jobs), mimetype='application/json')


# TODO
# @app.route('/job/requirement')
# def get_req():
#     job_requirement = json.dumps(pdc.get_jobs().pop().get_requirements())
#     return Response(job_requirement, mimetype='application/json')


@app.route('/pipelines', methods=[REST_GET])
def get_pipelines():

    # pipelines = {'pipelines': [
    #     pdc.get_outgoing_dict(), pdc2.get_outgoing_dict()]}
    pipelines = {'pipelines': [pipeline.get_outgoing_dict() for pipeline in pipeline_state.get_pipelines_()]}

    return Response(json.dumps(pipelines), mimetype='application/json')

# TODO
# @app.route('/pipeline_names', methods=[REST_GET])
# def get_pipeline_names():
#     pipelines = pipeline_state.get_pipeline_state_().items()
#     pipelines = json.dumps(pipelines)
#     return Response(pipelines, mimetype='application/json')
    # return {
    #     'pipelines': [pipeline.get_pipeline_name() for pipeline in pipeline_state.get_pipelines_()]
    #     }


@app.route('/pipelines', methods=[REST_POST])
def add_pipeline():
  
    if not request.json or not 'pipeline_name' in request.json:
        abort(400)

    name = request.json['pipeline_name']
    pdc = PipelineDataContainer()
    pdc.set_pipeline_name(name)
    pipeline_state.add_pipeline_container(pdc)

    return jsonify(pdc.get_outgoing_dict()), 201


if __name__ == '__main__':

    if DEBUG_MODE:
        # debug mode
        app.run(host=HOST_NUMBER, port=PORT_NUMBER, debug=True)

    else:
        # production mode
        print(f'Port: {PORT_NUMBER}')
        serve(app, port=PORT_NUMBER)
