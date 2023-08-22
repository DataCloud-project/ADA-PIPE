<p align="center"><img width=50% src="https://raw.githubusercontent.com/DataCloud-project/ADA-PIPE/main/figure/ADAPIPE_Logo_TransparentBackground_White.png"></p>&nbsp;

[![GitHub Issues](https://img.shields.io/github/issues/DataCloud-project/ADA-PIPE.svg)](https://github.com/DataCloud-project/ADA-PIPE/issues)
[![License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


1) In Windows OS and Linux OS, there are respectively these options to download the DSL file defined by [DEF-PIPE](https://github.com/DataCloud-project/DEF-PIPE-DSL/):

    * ```curl https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/example-v0.9.dsl -o D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\example-v0.9.dsl```

    * Or just through the [swagger](https://github.com/DataCloud-project/ADA-PIPE/blob/main/ImportFrom-DEF-PIPE/importing-from-def-pipe.PNG) -- current version of pipeline definition fetches the code through the API.

2) In the next step, run the ```parseDSL.py``` file for parsing the already-downloaded dsl, which extract the required features from the description.

3) The output of this code will be ``TelluPipeline.json`` consisting of three steps. 
