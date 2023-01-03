

1) In Windows OS, there is this option to download the file by running the following command:

* ```Invoke-WebRequest -URI https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/tellu.dsl -OutFile tellu.dsl```

In Linux OS, the following command works instead of ```Invoke_WebRequest```.
* ```wget https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/tellu.dsl```


2) In the next step, run the ```parseDSL.py``` file for parsing the already-downloaded dsl, which extract the required features from the description.
