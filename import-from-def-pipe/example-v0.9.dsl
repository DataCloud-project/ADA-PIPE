Pipeline PipelineOne {
	communicationMedium: medium WEB_SERVICE
	environmentParameters: {
		key_1: value_1,
		key_2: value_2
	}
	
	steps:
		- data-source step Step1
			implementation: container-implementation image: 'imageName'
			dataSource: inputDataSourceDB
			triggers: polling pollDatabase
				retries: 3
				interval: 3000
			resourceProvider: cloudProvider1
			previous: [Step3, Step2]
		- data-processing step Step2
			implementation: container-implementation image: 'imageName'
			resourceProvider: cloudProvider2
		- data-sink step Step3
		    implementation: container-implementation image: 'imageName'
			triggers: one-time '2022-05-01 12:00:00'
			resourceProvider: edgeProvider
		- data-sink step Step4
		    implementation: container-implementation image: 'imageName'
			triggers: interval-schedule
				frequency: SECOND
				interval: 1
				start-time: '2022-05-01 12:00:00'
		- data-sink step Step5
		    implementation: container-implementation image: 'imageName'
			triggers: cron-schedule 
				start-time: '2022-05-01 12:00:00'
				cron: '0 0 12 * * ?	'
			resourceProvider: fogProvider
			executionRequirement:
				hardRequirements:
					networkRequirement:
						min-bandwidth: 1.0
						max-bandwidth: 1.0
						min-latency: 1
						max-latency: 1
			 		qualitativeRequirement:
			 			min-benchmark: 1
			 			max-benchmark: 2
			 			cpu-architecture: 'arc'
			 			gpu-architecture: 'arc'
			 		quantitativeRequirement:
			 			min-cpu: 1.0
			 			max-cpu: 100.0
			 			gpu-availability: false
			 		osRequirement:
			 			os-type: 'type'
			 			is-64: 1
			 		verticalScale:
			 			min-cpu: 1.0
			 			min-ram-mb: 100
			 			min-storage-mb: 1000
			 		horizontalScale:
			 			min-instance: 1
			 			max-instance: 3
			 	
		- data-processing subPipeline SubPipelineOne
			implementation: container-implementation image: 'imageName'
			triggers: external-event
						
}


SubPipeline SubPipelineOne {
	implementation: container-implementation image: 'image_name'
}

PollDatabase pollDatabase {
	credential: databaseCredentials
	queryScriptName: 'None'
}

DatabaseCredentials databaseCredentials {	
}

InputDataSourceDatabase inputDataSourceDB {
	credential: databaseCredentials	
}

CloudProvider cloudProvider1 {
	providerLocation: 'location'
	mappingLocation: 'mapping'
}

CloudProvider cloudProvider2 {
	providerLocation: 'location'
	mappingLocation: 'mapping'
}

EdgeProvider edgeProvider {
	providerLocation: 'location'
	mappingLocation: 'mapping'
}

FogProvider fogProvider {
	providerLocation: 'location'
	mappingLocation: 'mapping'
}
