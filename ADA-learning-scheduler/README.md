<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/figure/ADAPIPE_Logo_TransparentBackground_White.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# ADA-PIPE learning-based Scheduler

This repository is for describing the adaptive machine-learning based schduler for data pipeline execution on the computing continuum.

We investigate a novel anomaly-detection based scheduling method to dynamically automate data pipeline processing across the computing continuum. 

## Scheduler

The scheduler is under development and [the current version](https://github.com/MyGodItsFull0fStars/alibaba_clusterdata/tree/double-prediction/cluster-trace-gpu-v2020/prediction) provides the prediction based on the resource utilization. 


## Architecture

The following figure shows that the learning-based adaptation approach is defined as a loop that cyclically updates every component contained in the loop.
The adaptation loop consists of the Big Data pipeline and the resources monitored by the Monitoring and Analysis component. The Big Data pipeline and the resources send the collected monitoring information as a state at a time step to the Monitoring and Analysis component. The Monitoring and Analysis component then uses these states and calculates an action as an update for the resource allocation to the Big Data pipeline.
![alt text](https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/ADA-learning-scheduler/ada-loop2.JPG)
