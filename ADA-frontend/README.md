

1) In Windows OS and Linux OS, there are respectively these options to download the DSL file defined by [DEF-PIPE](https://github.com/DataCloud-project/DEF-PIPE-DSL/):

    * ```curl https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/example-v0.9.dsl -o D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\example-v0.9.dsl```

    * Or just through the [swagger](https://github.com/DataCloud-project/ADA-PIPE/blob/main/ImportFrom-DEF-PIPE/importing-from-def-pipe.PNG) -- current version of pipeline definition fetches the code through the API.

2) In the next step, run the ```parseDSL.py``` file for parsing the already-downloaded dsl, which extract the required features from the description.
[Swagger_UI](http://194.182.187.139/swagger/) is  created to provide the API for connecting to other DataCloud tools.

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

## Redirecting the traffic
* To redirect the traffic from the default flask port number (5000) to the http port number (80), the following command were applied:

  * ``firewall-cmd --add-service=http --permanent``

  * ``firewall-cmd --add-service=https --permanent``

  * ``firewall-cmd --add-masquerade --permanent``

  * ``firewall-cmd --add-forward-port=port=80:proto=tcp:toport=5000 --permanent``

* To create the port forwarding on localhost:
 
  * ``iptables -t nat -I OUTPUT --source 127.0.0.1 --destination 127.0.0.1 -p tcp --dport 80 -j REDIRECT --to-ports 5000``

  * ``firewall-cmd --reload``
