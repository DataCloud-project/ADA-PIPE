# ADA-PIPE-Frontend

The web interface to provision resources for microservices on the Computing Continuum.

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

``pip3.9 install -U scipy numpy PyYaml flask pandas``

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
