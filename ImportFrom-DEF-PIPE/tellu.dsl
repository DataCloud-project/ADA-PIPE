Pipeline TELLU {
	communicationMedium: medium WEB_SERVICE
	environmentParameters: {
		key_1: value_1,
		key_2: value_2
	}
	steps:
		- data-source step GenerateSampledataReformatPushinMQTT
			implementation: container-implementation image: 'registry.sintef.cloud/tellucare-edge'
			environmentParameters: {
				MQTT_HOST: 'oslo.sct.sintef.no',
				MQTT_USERNAME: 'TGW000000000', 
				MQTT_CLIENT_ID: 'TGWDATACLOUD',
				MQTT_PASS: '???',
				MQTT_PORT: '1883'
			}
			resourceProvider: TelluGateway0
			executionRequirement:
				hardRequirements:
					horizontalScale:
						min-instance: 1
						max-instance: 1
			
		- data-processing step ReceiveDataFromMQTTCheckPatientPlanBuildFhirDBrecordsStoretoFhirDB
			implementation: container-implementation image: 'registry.sintef.cloud/tellucare-api:latest'
			environmentParameters: {
				RABBITMQ_HOST: 'oslo.sct.sintef.no:5672', 
				RABBITMQ_USERNAME: 'tellucareapi', 
				RABBITMQ_PASSWORD: '???', 
				FHIR_URL: 'https://tellucloud-fhir.sintef.cloud' 
			}
			resourceProvider: TelluCloudProvider
			previous: [GenerateSampledataReformatPushinMQTT]
			executionRequirement:
				hardRequirements:
			 		quantitativeRequirement:
			 			min-cpu: 1000.0
			 			max-cpu: 1024.0
			 			min-ram-mb: 8192
			 			gpu-availability: false
			 		horizontalScale:
			 			min-instance: 1
			 			max-instance: 10
			 			
		- data-processing step AnalyzeandCreateNotificationforHealthcarePersonnel
			implementation: container-implementation image: 'registry.sintef.cloud/tellucare-application-logic:latest'
			environmentParameters: {
				RABBITMQ_HOST: 'oslo.sct.sintef.no:5672', 
				RABBITMQ_USERNAME: 'tellucareapi', 
				RABBITMQ_PASSWORD: '???', 
				FHIR_URL: 'https://tellucloud-fhir.sintef.cloud' 
			}
			resourceProvider: TelluCloudProvider
			previous: [ReceiveDataFromMQTTCheckPatientPlanBuildFhirDBrecordsStoretoFhirDB]
			
			executionRequirement:
				hardRequirements:
			 		quantitativeRequirement:
			 			min-cpu: 500.0
			 			max-cpu: 512.0
			 			min-ram-mb: 1024
			 			gpu-availability: false
			 		horizontalScale:
			 			min-instance: 1
			 			max-instance: 5	
}