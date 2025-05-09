<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/figure/ADAPIPE_Logo_TransparentBackground_White.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


We received the monitoring information from the application execution on the computing continuum.

Requirements are as follows:

``python3.9, numpy, scipy, pyyaml, pandas, prometheus_api_client, seaborn``


To scrape the NetData metrics, we configured the [Prometheus](https://learn.netdata.cloud/docs/exporting-data/prometheus#configure-prometheus-to-scrape-netdata-metrics).


To install the netdata-pandas library for collecting metrics:
``pip3 install netdata-pandas``


To analyze the data and run the ML model:
``pip3 install -U scikit-learn``

The recorded data and their related analyses are available as follows:
  * [DeviceData](https://zenodo.org/records/14961415/files/DeviceData.csv)
  * ``elbow_kmeans.ipynb``  
