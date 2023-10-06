import time
import random
import json
import re
import subprocess
from subprocess import call
import sys
import os
import numpy
import requests
import logging
from kubernetes import client, config, watch
from prometheus_api_client import PrometheusConnect

start_time = time.monotonic()

prom = PrometheusConnect()

config.load_kube_config()
v1=client.CoreV1Api()

scheduler_name = "ads"

def nodes_available():
    ready_nodes = []
    for n in v1.list_node().items:
            for status in n.status.conditions:
                if status.status == "True" and status.type == "Ready":
                    ready_nodes.append(n.metadata.name)
    #print("available nodes: ",ready_nodes)
    return ready_nodes

def scheduler(pod, node, namespace="default"):
    # print ("start binding")
    try:
        target = client.V1ObjectReference()
        target.kind = "Node"
        target.apiVersion = "v1"
        target.api_version = 'v1'
        target.name = node
        #print ("Target object: ", target)
        if target.name != '':
            meta = client.V1ObjectMeta()
            meta.name = pod.metadata.name
            body = client.V1Binding(target=target, metadata=meta)
            v1.create_namespaced_binding(namespace, body, _preload_content=False)
            print(meta.name, " scheduled on ", node)
        #else:
        #   print(pod.metadata.name, " not scheduled")
    except client.rest.ApiException as e:
        print(json.loads(e.body)['message'])
        print("------------------------------------------")
    return

def scale():
    #print(nodes_available())
    apps_v1 = client.AppsV1Api()
    #autoscaler_status = requests.get(f"http://10.107.50.125:5000/").json()
    #print (autoscaler_status)
    resource_requests = dict()
    # read deployment
    call(["kubectl", "delete", "deployments.apps", "tellucare-application-logic-deployment"]) 
    call(["kubectl", "apply", "-f", "/home/edgegateway/Documents/NaMe/project/v0.2.0/deployment.yaml"])
    ret = apps_v1.list_namespaced_deployment(namespace="default")
    #print (ret.items)
    for i in ret.items:
        deployment = apps_v1.read_namespaced_deployment(name=i.metadata.name, namespace="default")
        #print (deployment.metadata.name)
        update_deployment(deployment.metadata.name, 500, 64, 2, False)


def update_deployment(deployment_name: str, cpu_limit: int, memory_limit: int,
                          number_of_replicas: int, replace: bool) -> client.V1Deployment:
    """Updates a given deployment with given values for replicas, cpu limit and replicas limit.
    Args:
      replace: if the deployment should be replaced or patched
      deployment_name: name of deployment
      cpu_limit: new cpu limit
      memory_limit: new memory limit
      number_of_replicas: new number of replicas
      deployment_name: str:
      cpu_limit: int:
      memory_limit: int:
      number_of_replicas: int:
      replace: bool:
    Returns:
      None
    """
    # init API
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    # read deployment
    deployment = apps_v1.read_namespaced_deployment(name=deployment_name, namespace="default")
    # get resource requests
    resource_requests = get_resource_requests()
    resource_requests = resource_requests[deployment_name]
    # updates cpu and memory limits
    #print (resource_requests["cpu"]," ",resource_requests["memory"])
    new_resources = client.V1ResourceRequirements(
        #requests={"cpu": resource_requests["cpu"], "memory": resource_requests["memory"]},
        requests={"cpu": f"{cpu_limit}m", "memory": f"{memory_limit}Mi"},
        limits={"cpu": f"{cpu_limit}m", "memory": f"{memory_limit}Mi"}
    )
    deployment.spec.template.spec.containers[0].resources = new_resources
    # updates number of replicas
    deployment.spec.replicas = number_of_replicas
    if not replace:
        # updates the deployment
        try:
            api_response = apps_v1.patch_namespaced_deployment(
                name=deployment_name,
                namespace="default",
                body=deployment)
            logging.info(f"Deployment updated of {deployment_name}.")
            logging.debug(f"f Deployment update: {api_response.status}")
            #print(api_response)
        except Exception as err:
            logging.info(f"Error while deployment: {err}")
    else:
        try:
            api_response = apps_v1.replace_namespaced_deployment(
                name=deployment_name,
                namespace="default",
                body=deployment)
            logging.info(f"Deployment updated of {deployment_name}.")
            logging.debug(f"f Deployment update: {api_response.status}")
        except Exception as err:
            logging.info(f"Error while deployment: {err}")
    return deployment

def get_resource_requests():
    apps_v1 = client.AppsV1Api()
    resource_requests = dict()
    # read deployment
    ret = apps_v1.list_namespaced_deployment(namespace="default")
    for i in ret.items:
        deployment = apps_v1.read_namespaced_deployment(name=i.metadata.name, namespace="default")
        resources = deployment.spec.template.spec.containers[0].resources.requests
        resource_requests[i.metadata.name] = resources
        #print (deployment.spec.template.spec.containers[0])
    #print (resource_requests)
    return resource_requests

def main():
    print(nodes_available())
    print()
    scale()
    print()
    call(["kubectl", "get", "deployments.apps"])

if __name__ == '__main__':
    main()

elapsed_time = numpy.round(time.monotonic() - start_time , 5)
#print ("=====================================================================")
#print ("Algorithm execution time: {} second(s)".format(elapsed_time))
#print ("=====================================================================")
