

1) In Windows OS and Linux OS, there are respectively these options to download the DSL file defined by [DEF-PIPE](https://github.com/DataCloud-project/DEF-PIPE-DSL/):

* ```Invoke-WebRequest -URI https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/tellu.dsl -OutFile tellu.dsl```

* ```wget https://raw.githubusercontent.com/DataCloud-project/DEF-PIPE-DSL/master/XText/se.kth.datacloud.dsl/src/se/kth/datacloud/dsl/tellu.dsl```

* Or just through the [swagger ui](https://github.com/DataCloud-project/ADA-PIPE/blob/main/ImportFrom-DEF-PIPE/importing-from-def-pipe.PNG)

2) In the next step, run the ```parseDSL.py``` file for parsing the already-downloaded dsl, which extract the required features from the description.
