import numpy
from operator import itemgetter  
from matching.games import HospitalResident
import yaml

microservices = ["encoding", "splittingstream", "training"]



encode = [2.69,3.16,20.64,28,60] #seconds
splittingstream = [11.7,  11.2, 3.1,   3.1,   3.1 ] #seconds
training = [33.23, 56.746 , 232.253 , 466.830 , 1000] #seconds

#              0	 1	2     3     4 
resources = ["DataCloud-wp1","DataCloud-wp2","DataCloud-edge-0","DataCloud-edge-1","DataCloud-edge-2"]


lat = [85e-3,60e-3,60e-3,60e-3] #ms


#https://aws.amazon.com/kinesis/data-firehose/pricing/?nc=sn&loc=3

index_of_segment = 4

seg_size = [286720, 2457600, 3440640, 14400000, 20971520 ] #bits
video_size = [2000000, 14000000, 28000000, 60000000, 204800000] #bits

#Number of frames per video
SIZE = 200


BW_r = [60000000 , 920000000, 450000000 , 800000000 , 328000000]#bps


dictlistResources = list( {} for i in range(len(resources)) )
sorted_dictlistResources = list( {} for i in range(len(resources)) )
dictlistMicroservices = list( {} for i in range(len(microservices)) )
sorted_dictlistMicroservices = list( {} for i in range(len(microservices)) )


T = [[0] * len(resources) for i in range(len(microservices))]

T[0][0] = encode[0] + ((video_size[4])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[0][1] = encode[1] + ((video_size[4])/BW_r[1]) + (lat[1]) + (lat[1])
T[0][2] = encode[2] + ((video_size[4])/BW_r[2]) + (1e-3)
T[0][3] = encode[3] + ((video_size[4])/BW_r[3]) + (1e-3)

T[1][0] = splittingstream[0] +  (60*(seg_size[index_of_segment])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[1][1] = splittingstream[1] +  (60*(seg_size[index_of_segment])/BW_r[1]) + (lat[1]) + (lat[1])
T[1][2] = splittingstream[2] +  (60*(seg_size[index_of_segment])/BW_r[2]) + (1e-3) + (1e-3)
T[1][3] = splittingstream[3] +  (60*(seg_size[index_of_segment])/BW_r[3]) + (1e-3) + (1e-3)

T[2][0] = training[0] + (60*(seg_size[index_of_segment])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[2][1] = training[1] + (60*(seg_size[index_of_segment])/BW_r[1]) + (lat[1]) + (lat[1])
T[2][2] = training[2] + (60*(seg_size[index_of_segment])/BW_r[2]) + (1e-3) + (1e-3)
T[2][3] = training[3] + (60*(seg_size[index_of_segment])/BW_r[3]) + (1e-3) + (1e-3)

fileObject = open("D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\steps.yml", 'w').close()
fileObject = open("D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\resources.yml",'w').close()
	
#sorted(iterable, *, key=None, reverse=False)
for i in range(len(microservices)):
	for j in range(len(resources)):		
		dictlistMicroservices[i][(resources[j],microservices[i])] = numpy.round((T[i][j]),4)
	sorted_dictlistMicroservices[i]=sorted(dictlistMicroservices[i].items(),key = itemgetter(1))
	mpllll=dict(dict(sorted_dictlistMicroservices[i]).keys())
	listofvalues = list(mpllll.keys())
	listofkeys=list(mpllll.values())
	dicttttt= {listofkeys[0]:listofvalues}
	with open(r'D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\steps.yml', 'a') as file:
		documents = yaml.dump(dicttttt, file)
		file.close()

for j in range(len(resources)):
		for i in range(len(microservices)):
			dictlistResources[j][(microservices[i],resources[j])] = numpy.round((BW_r[j]) - ( SIZE*(seg_size[index_of_segment])),4)
		sorted_dictlistResources[j]=sorted(dictlistResources[j].items(),key = itemgetter(1))
		dpllll = dict(dict(sorted_dictlistResources[j]).keys())
		listofvalues = list(dpllll.keys())
		listofkeys = list(dpllll.values())
		dicttttt = {listofkeys[0]:listofvalues}
		with open(r'D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\resources.yml', 'a') as file:
			documents = yaml.dump(dicttttt, file)
			file.close()


resident__ = (open('D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\steps.yml', 'r'))
resident_preferences = yaml.full_load(resident__)
resident__.close()
hospital__ = (open('D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\resources.yml', 'r'))
hospital_preferences = yaml.full_load(hospital__)
hospital__.close()
hospital_cap = (open('D:\\00Research\\matching\\scheduler\\ADA-PIPE-Frontend-new\\MOG-BC2\\match-model\\capacities.yml', 'r'))
hospital_capacities = yaml.full_load(hospital_cap)
hospital_cap.close()

game = HospitalResident.create_from_dictionaries(
    resident_preferences, hospital_preferences, hospital_capacities
)

matching0 = game.solve(optimal="resident")

summatch = 0
if(T[0][1] != 0 and T[1][0] != 0 and T[2][1] != 0 ):
		summatch = T[0][1] + T[1][0] + T[2][1] - (2*lat[1]) - (2*lat[1]) 


print()
#print("------------------Time------------------")
print("match: "    ,numpy.round(summatch,4))
#print("----------------------------------------")
print()

print(matching0)
print()
print()