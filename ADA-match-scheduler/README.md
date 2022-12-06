<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/figure/ADAPIPE_Logo_TransparentBackground_White.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# ADA-PIPE Match Scheduler

Provides a capacity-aware matching-based scheduler for data pipeline processing across the computing continuum.

# Installation

* Operating systems:
  * [NVIDIA Jetson Linux](https://developer.nvidia.com/embedded/linux-tegra) for NVIDIA devices;

  * [Raspberry Pi OS](https://www.raspberrypi.com/software/) for RPi devices.

* Docker and Kubenetes:

  * [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/);

  * [Kubernetes on Ubuntu](https://phoenixnap.com/kb/install-kubernetes-on-ubuntu) for x86_64 Cloud or Fog instances, and [Kubernetes on (vanilla) Raspbian Lite (https://github.com/alexellis/k8s-on-raspbian/blob/master/GUIDE.md) for the Edge devices;


# Tool info

The base model of the matching-based scheduler requires Python libraries such as ``networkx, operator, numpy, yaml, json``.

Integrating ada-match-scheduler to Kubernetes scheduler:

* Matching library by package installer for Python 3.9 (pip3.9);

* Measuring bandwidth and latency between the devices by: [kube-latency](https://github.com/simonswine/kube-latency);

* Monitoring the cluster by the [Prometheus operator v0.45.0](https://github.com/prometheus-operator/prometheus-operator); 

* Transmitting data between pipeline steps through an asynchronous message queue platform [KubeMQ v2.2.10](https://github.com/kubemq-io/kubemq-community/releases/tag/v2.2.10).

At the end, Python script "scheduling.py" collects the monitoring information by [Prometheus Python API](https://pypi.org/project/prometheus-api-client/) from the local {Kubernetes} Edge cluster, and then utilizes the [Python client library v17.17 for Kubernetes](https://github.com/kubernetes-client/python) to execute the customized ada-match scheduler and deploy the application pods on the appropriate devices.
