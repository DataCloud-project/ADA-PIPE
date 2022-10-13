PIPELINE_NAME: str = 'pipelineName'
PIPELINE_TYPE: str = 'pipelineType'
CHUNK_NAME: str = 'chunkName'

TERMINATION_CHECK: str = 'terminationCheck'

TIME: str = 'time'
ESTIMATED_START_TIME: str = 'EST'
ESTIMATED_FINISH_TIME: str = 'EFT'
TERMINATION_TIME: str = 'TT'

STEPS_LIST_KEY: str = 'stepsList'
STEPS_ORDER: str = 'order'
STEPS_NAME: str = 'name'
STEPS_RESOURCE: str = 'resource'
STEPS_ARCHITECTURE: str = 'architecture'
STEPS_ELASTICITY_CONTROLLER_MODE: str = 'elasticityControllerMode'
STEPS_DOCKER_IMAGE: str = 'dockerImage'
STEPS_DOCKER_CREDENTIALS: str = 'dockerCredentialsUsing'
STEPS_DOCKER_USERNAME: str = 'dockerUsername'
STEPS_DOCKER_PASSWORD: str = 'dockerPassword'  # yikes
STEPS_DOCKER_CUSTOM_REGISTRY: str = 'dockerCustomRegistry'
STEPS_REGISTRY: str = 'dockerRegistry'
STEPS_REQUIREMENTS: str = 'requirement'
STEPS_VIRTUAL_CPUS: str = 'vCPUs'
STEPS_RAM: str = 'ram'
STEPS_STORAGE: str = 'storage'
STEPS_HEALTH_CHECK: str = 'healthCheck'
STEPS_TERMINATION_CHECK: str = 'terminationCheck'
STEPS_COMMAND: str = 'command'
STEPS_ENVIRONMENT_VARIABLES: str = 'environmentalVariables'
STEPS_NUM_WORKERS: str = 'numWorkers'

STEPS_EXPOSED_INTERFACES: str = 'exposedInterfaces'
STEPS_EXPOSED_INTERFACES_NAME: str = 'name'
STEPS_EXPOSED_INTERFACES_PORT: str = 'port'
STEPS_EXPOSED_INTERFACES_TYPE: str = 'interfaceType'
STEPS_EXPOSED_INTERFACES_TRANSMISSION_PROTOCOL: str = 'transmissionProtocol'

STEPS_REQUIRED_INTERFACES: str = 'requiredInterfaces'
STEPS_PLUGIN: str = 'plugin'
STEPS_DEVICES: str = 'devices'
STEPS_VOLUMES: str = 'volumes'
STEPS_LABEL: str = 'label'
STEPS_HOSTNAME: str = 'hostname'
STEPS_CAPABILITY_DROPS: str = 'capabilityDrops'
STEPS_CAPABILITY_ADDS: str = 'capabilityAdds'
STEPS_ULIMIT_MEMLOCK_SOFT: str = 'ulimitMemlockSoft'
STEPS_ULIMIT_MEMLOCK_HARD: str = 'ulimitMemlockHard'
STEPS_NETWORK_MODE_HOST: str = 'networkModeHost'
STEPS_PRIVILEGE: str = 'privilege'

# job_keys: list = [
#     JOB_LIST_KEY, JOB_ORDER,
#     JOB_NAME,
#     JOB_RESOURCE,
#     JOB_ARCHITECTURE,
#     JOB_ELASTICITY_CONTROLLER_MODE,
#     JOB_DOCKER_IMAGE,
#     JOB_DOCKER_CREDENTIALS,
#     JOB_DOCKER_USERNAME,
#     JOB_DOCKER_PASSWORD,   # yikes
#     JOB_DOCKER_CUSTOM_REGISTRY,
#     JOB_REGISTRY,
#     JOB_REQUIREMENTS,
#     JOB_VIRTUAL_CPUS,
#     JOB_RAM, JOB_STORAGE,
#     JOB_HEALTH_CHECK,
#     JOB_TERMINATION_CHECK,
#     JOB_COMMAND,
#     JOB_ENVIRONMENT_VARIABLES,
#     JOB_NUM_WORKERS,

#     JOB_EXPOSED_INTERFACES,
#     JOB_EXPOSED_INTERFACES_NAME,
#     JOB_EXPOSED_INTERFACES_PORT,
#     JOB_EXPOSED_INTERFACES_TYPE,
#     JOB_EXPOSED_INTERFACES_TRANSMISSION_PROTOCOL,

#     JOB_REQUIRED_INTERFACES,
#     JOB_PLUGIN,
#     JOB_DEVICES,
#     JOB_VOLUMES,
#     JOB_LABEL,
#     JOB_HOSTNAME,
#     JOB_CAPABILITY_DROPS,
#     JOB_CAPABILITY_ADDS,
#     JOB_ULIMIT_MEMLOCK_SOFT,
#     JOB_ULIMIT_MEMLOCK_HARD,
#     JOB_NETWORK_MODE_HOST,
#     JOB_PRIVILEGE]
