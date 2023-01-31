<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/figure/ADAPIPE_Logo_TransparentBackground_White.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# ADA-PIPE-Frontend

The web interface to provision resources for data pipeline's steps on the Computing Continuum.


[Swagger_UI](http://194.182.187.139:5000/swagger/) is  created to provide the API for connecting to other DataCloud tools.

We utilized a [video tutorial](https://www.youtube.com/watch?v=AyyX9yM_OZk) and a [document on realpython website](https://realpython.com/flask-connexion-rest-api/).

Moreover, we used the Bootsrap features by following a [video tutorial](https://www.youtube.com/watch?v=kMsKm53XtyA) and a [document on creating a simple web page using Bootstrap](https://www.blog.duomly.com/how-to-crate-simple-web-page-using-bootstrap-5/).


## Installation
The main script is ``demo.py``.

Requirements are ``python3.9, matching, numpy, scipy, pyyaml, pandas, flask, waitress python-keycloak, flask-oidc`` as follows:

``sudo apt update``

``sudo apt install software-properties-common``

``sudo wget -c https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh``

``sudo chmod +x Miniconda3-latest-Linux-x86_64.sh``

``./Miniconda3-latest-Linux-x86_64.sh``

``source ./.bashrc``

``python3 --version``

``sudo add-apt-repository ppa:deadsnakes/ppa``

``sudo apt install python3-pip``

``sudo apt-get install python3.9-distutils``

``curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py``

``python3.9 get-pip.py``

``python3.9 -m pip install numpy``

``python3.9 -m pip matching``

``pip3.9 install -U scipy numpy PyYaml flask pandas Werkzeug flask-swagger-ui``

``flask run -h 194.182.187.139``

``export FLASK_APP=server``

``flask run``

``conda install -c conda-forge flask_cors -y``

``conda install -c anaconda waitress``

``pip3.9 install requests==2.25.1 urllib3==1.26.5``

``pip3.9 install python-keycloak flask-oidc``



## KeyCloak
To test the KeyCloak:

``python3.9 test_keycloak.py``

## Redirect traffic
* To redirect the traffic from the default flask port number (5000) to the http port number (80), the following command were applied:

  * ``firewall-cmd --add-service=http --permanent``

  * ``firewall-cmd --add-service=https --permanent``

  * ``firewall-cmd --add-masquerade --permanent``

  * ``firewall-cmd --add-forward-port=port=80:proto=tcp:toport=5000 --permanent``

* Create the port forwarding on localhost:
 
  * ``iptables -t nat -I OUTPUT --source 127.0.0.1 --destination 127.0.0.1 -p tcp --dport 80 -j REDIRECT --to-ports 5000``

  * ``firewall-cmd --reload``
