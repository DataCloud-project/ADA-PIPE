<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/figure/ADAPIPE_Logo_TransparentBackground_White.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Resource utilization prediction model

This repository describes the machine-learning-based resource prediction for data pipeline execution on the computing continuum.

[The full version of the scheduler](https://github.com/MyGodItsFull0fStars/alibaba_clusterdata/tree/double-prediction/cluster-trace-gpu-v2020/prediction) provides the prediction based on the resource utilization and corrects the user allocated resource parameters to values closer to the actual values. It uses a **Long-Short Term Memory** machine learning model.

### Installation of the Environment

We use the Python dependency framework [anaconda installation](https://docs.anaconda.com/anaconda/install/index.html) to install the environment.

Then execute the command `conda env create --file=environment.yml`. The CLI will ask you to accept installing the environment; please accept it, and after doing so, the environment will be installed on your system.

After the environment's installation, you can activate it with `conda activate lstm_prediction`. 


Since Jupyter dependency is also included in this environment, select the Python kernel `lstm_prediction` to execute the code inside the notebook.
