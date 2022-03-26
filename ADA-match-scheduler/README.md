<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/toolbox/master/docs/img/datacloud_logo.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# ADA-PIPE Match Scheduler

Provides a capacity-aware macthing-based scheduler for data pipeline processing across the computing continuum.

# How_to

Integrating ada-matach-scheduler to Kubernetes scheduler:

[![Docker v20.10.12](https://www.docker.com/)] on all devices and instances;

Measuring bandwidth and latency between the local Edge devices: [![kube-latency](https://github.com/simonswine/kube-latency)];

Monitoring local Edge cluster by the [![Prometheus operator v0.45.0](https://github.com/prometheus-operator/prometheus-operator)]; 

Python script "scheduling.py" collects the monitoring information by [![Prometheus Python API](https://pypi.org/project/prometheus-api-client/)] from the local {Kubernetes} Edge cluster, and then utilizes the [![Python client library v17.17 for Kubernetes](https://github.com/kubernetes-client/python)] to execute the customized ada-matach-scheduler scheduler and deploy the application pods on the appropriate devices;

[![Transmitting data through an asynchronous message queue platform [![KubeMQ v2.2.10](https://github.com/kubemq-io/kubemq-community/releases/tag/v2.2.10)]
