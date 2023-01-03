import sys
sys.path.append('./interface_constants')
from interface_constants import *
import json
# cleanup of unused imports is highly recommended
# all of the imports below are unused
# if your editor does not show this, a linter might be a good extension to install ;)
from typing import List, Dict
from copy import copy, deepcopy
import yaml

# don't mix coding styles (camelCase with snake_case ;) )
inFile = "D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\tellu.dsl"

with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json', 'r') as openfile:
			requirement_settings = json.load(openfile)
            # when you use with open(...) you don't need to close the file yourself,
            # since with open will work as a guard/scope that will only open when successful, 
            # and also closes the files itself
			openfile.close() # plus you forgot to call the `close` method using parenthesis

count = 0
# In general, I'd move the parsing to a method, that uses multiple helper functions depending on the nesting level
# that have a narrow scope of responsibility
with open(inFile, "r") as fp:
    # in my opinion, while True is not advisable in this case (for parsing a file).
    # you could do something like `while line := fp.readline()`
    # this would omit the conditional check if not line, and remove some lines
    # this works since the ':=' operator creates the line variable and assigns it the value of fp.readline() 
    # in each loop iteration and line will also only live in this scope (which it already does)
    while True:
        
        # could be removed if proposition from above is implemented
        line = fp.readline()
        if not line:
            break
        
        words = line.strip().split(" ")
        
        # requirement_settings["stepsList"][0] could be assigned to a variable, since it is used in 7 lines already 
        # and to improve readability
        if  len(words) != 1:
            if (words[0] == STEPS_REQ_MAXCPU):
                # there is a lot going on in this line of code
                # maybe split it into two lines (creation of value and then assign the value)
                requirement_settings["stepsList"][0]["requirement"]["vCPUs"]=((float(words[1]))/1024.0)
                # remove commented code fragment
                #print(requirement_settings["stepsList"][0]["requirement"]["vCPUs"])
            elif (words[0] == STEPS_REQ_MINMEM):
                requirement_settings["stepsList"][0]["requirement"]["ram"] = words[1]
                # remove commented code fragment
                #print(requirement_settings["stepsList"][0]["requirement"]["ram"])
            elif (words[0] == STEPS_IMPLEMENTATION):
                requirement_settings["stepsList"][0]["dockerImage"] = words[3].lower()
                # remove commented code fragment
                #print(requirement_settings["stepsList"][0]["dockerImage"])
 
        # be aware that this if-else condition writes to the dictionary fields each loop iteration
        # which is not necessary
        if (count == 0):
            # count might not be a good name, since it does not represent what its responsibility or function is
            requirement_settings["stepsList"][0]["provider"] = "Tellu" 
            requirement_settings["stepsList"][0]["resource"] = "Tellu Gateway 0" 
        else:
            requirement_settings["stepsList"][0]["provider"] = "DataCloud-k8s"
            requirement_settings["stepsList"][0]["resource"] = "DataCloud-k8s-1"
            
        if "data-processing step" in line or "data-source step" in line:
            count += 1
            # remove commented code fragment
            #print(count)
with open("D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\3ApplicationLogic.json", "w") as outfile:
			json.dump(requirement_settings,outfile)
			outfile.close()
# remove commented code fragment
#with open('D:\\00Research\\matching\\scheduler\\Demo3\\dsl2json\\requirements.yaml', 'r') as file_read:
#	requirement_list = yaml.load(file_read, Loader=yaml.FullLoader)#json.dumps(yaml.load(file_read, Loader=yaml.FullLoader))
#print((requirement_list))
