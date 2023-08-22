from typing import List, Dict
from interface_json import PipelineDataContainer, StepsDataContainer
from copy import copy, deepcopy


class PipelineState():

    def __init__(
                self, 
                initial_pipeline_state: Dict[str, PipelineDataContainer] = None, 
                add_dummy_data: bool = False
                ) -> None:
        if initial_pipeline_state is None:
            initial_pipeline_state = {}
        self.__pipelines: Dict[str, PipelineDataContainer] = initial_pipeline_state

        if add_dummy_data is True:
            self.__init_with_dummy_data()

    def add_pipeline_container(self, pipeline: PipelineDataContainer):
        name = pipeline.get_pipeline_name()
        self.__pipelines[name] = pipeline

    def get_pipeline_state(self) -> Dict[str, PipelineDataContainer]:
        return deepcopy(self.get_pipelines)

    def get_pipeline_state_(self) -> Dict[str, PipelineDataContainer]:
        return self.__pipelines

    def get_pipelines(self) -> List[PipelineDataContainer]:
        return deepcopy(self.__pipelines.values())

    def get_pipelines_(self) -> List[PipelineDataContainer]:
        return self.__pipelines.values()

    def __get__(self, pipeline_name: str) -> PipelineDataContainer:
        return self.__pipelines[pipeline_name]

    def __init_with_dummy_data(self):
        pdc = PipelineDataContainer()
        pdc2 = PipelineDataContainer()
        # pdc.set_pipeline_name('first pipeline')
        pdc2.set_pipeline_name('second_pipeline')
        self.add_pipeline_container(pdc)
        self.add_pipeline_container(pdc2)
