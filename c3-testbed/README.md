# c3-testbed

The Carinthian Computing Continuum (C3) infrastructure as a research laboratory and infrastructure provides the Cloud, Fog, and Edge computing:

https://c3.itec.aau.at/index.php/infrastructure/

https://edge.itec.aau.at/

# Devices/instances:

The resources are as follows:

AWS instances are located in Frankfurt and London, Google instances located in Frankfurt, Exoscale Edge-Cloud located in Klagenfurt, Vienna, Frankfurt, Zurich, Geneva, Sofia, local OpenStack instances located in the University of Klagenfurt along with the Edge device such as Nvidia Jetson Nano, RPi4, RPi3 (mounted with Coral accelators).

# Dataset

[Edge infrastructure traces](https://zenodo.org/record/7311294)

Zahra Najafabadi Samani, Narges Mehran, Dragi Kimovski, Josef Hammer, and Radu Prodan. [Dataset] (version 1), Zenodo, November 2022.


# Citation

Kimovski. D., Matha. R., Hammer. J., Mehran. N., Hellwagner. H., and Prodan. R., ["Cloud, Fog, or Edge: Where to Compute?,"](https://ieeexplore.ieee.org/document/9321525/) IEEE Internet Computing, vol. 25, no. 4, pp. 30–36, 2021.

```
@article{Kimovski2021WhereToCompute,
author = {Kimovski, Dragi and Matha, Roland and Hammer, Josef and Mehran, Narges and Hellwagner, Hermann and Prodan, Radu},
doi = {10.1109/MIC.2021.3050613},
eprint = {2101.10417},
issn = {19410131},
journal = {IEEE Internet Computing},
keywords = {Benchmarking,Carbon footprint,Cloud computing,Edge computing},
number = {4},
pages = {30--36},
title = {{Cloud, Fog, or Edge: Where to Compute?}},
volume = {25},
year = {2021}
}
```

Mehran, N., Samani, Z.N., Kimovski, D. and Prodan, R., 2022, September. Matching-based Scheduling of Asynchronous Data Processing Workflows on the Computing Continuum. In 2022 IEEE International Conference on Cluster Computing (CLUSTER) (pp. 58-70). IEEE. [https://doi.org/10.1007/978-3-031-12597-3_15](https://ieeexplore.ieee.org/abstract/document/9912724)

BibTex:
```
@INPROCEEDINGS{9912724,  
author={Mehran, Narges and Najafabadi Samani, Zahra  and Kimovski, Dragi and Prodan, Radu},  
booktitle={2022 IEEE International Conference on Cluster Computing (CLUSTER)},   
title={Matching-based Scheduling of Asynchronous Data Processing Workflows on the Computing Continuum},   
year={2022},  
volume={},  
number={},  
pages={58-70},  
abstract={Today's distributed computing infrastructures en-compass complex workflows for real-time data gathering, transferring, storage, and processing, quickly overwhelming centralized cloud centers. Recently, the computing continuum that federates the Cloud services with emerging Fog and Edge devices represents a relevant alternative for supporting the next-generation data processing workflows. However, eminent challenges in automating data processing across the computing continuum still exist, such as scheduling heterogeneous devices across the Cloud, Fog, and Edge layers. We propose a new scheduling algorithm called C3 -MATCH, based on matching theory principles, involving two sets of players negotiating different utility functions: 1) workflow microservices that prefer computing devices with lower data processing and queuing times; 2) computing continuum devices that prefer microservices with corresponding resource requirements and less data transmission time. We evaluate $C^{3}$-MATCH using real-world road sign inspection and sentiment analysis workflows on a federated computing continuum across four Cloud, Fog, and Edge providers. Our combined simulation and real execution results reveal that $C^{3}$-MATCH achieves up to 67% lower completion time than three state-of-the-art methods with 10 ms-1000 ms higher transmission time.},  
keywords={},  
doi={10.1109/CLUSTER51413.2022.00021},  
ISSN={2168-9253},  
month={Sep.},}
```


Samani, Z.N., Mehran, N., Kimovski, D. and Prodan, R., 2023, May. Proactive SLA-aware Application Placement in the Computing Continuum. In 37th IEEE International Parallel & Distributed Processing Symposium (IPDPS). [https://doi.org/10.1109/IPDPS54959.2023.00054](https://ieeexplore.ieee.org/abstract/document/10177411)

BibTex:
```
@INPROCEEDINGS{10177411,  
author={Samani, Zahra Najafabadi and Mehran, Narges and Kimovski, Dragi and Prodan, Radu},  
booktitle={37th IEEE International Parallel & Distributed Processing Symposium (IPDPS)},   
title={Proactive SLA-aware Application Placement in the Computing Continuum},   
year={2023},  
volume={},  
number={},  
pages={468-479},  
abstract={.},  
keywords={},  
doi={10.1109/IPDPS54959.2023.00054}, }
```

Zahra Najafabadi Samani, et al. "Incremental multilayer resource partitioning for application placement in dynamic fog." IEEE Transactions on Parallel and Distributed Systems 34.6 (2023): 1877-1896.
```
@article{samani2023incremental,
  title={Incremental multilayer resource partitioning for application placement in dynamic fog},
  author={Samani, Zahra Najafabadi and Mehran, Narges and Kimovski, Dragi and Benedict, Shajulin and Saurabh, Nishant and Prodan, Radu},
  journal={IEEE Transactions on Parallel and Distributed Systems},
  volume={34},
  number={6},
  pages={1877--1896},
  year={2023},
  publisher={IEEE}
}
```

Zahra Najafabadi Samani, Narges Mehran, Dragi Kimovski, Josef Hammer, & Radu Prodan. (2022). Edge infrastructure traces (Version 1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7311294

```
@dataset{zahra_najafabadi_samani_2022_7311294,
  author       = {Zahra Najafabadi Samani and
                  Narges Mehran and
                  Dragi Kimovski and
                  Josef Hammer and
                  Radu Prodan},
  title        = {Edge infrastructure traces},
  month        = nov,
  year         = 2022,
  publisher    = {Zenodo},
  version      = 1,
  doi          = {10.5281/zenodo.7311294},
  url          = {https://doi.org/10.5281/zenodo.7311294}
}
```

Josef Hammer, Narges Mehran, Dragi Kimovski, Radu Prodan, & Hermann Hellwagner. C3-Edge–An Automated Mininet-Compatible SDN Testbed on Raspberry Pis and Nvidia Jetsons. In NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium, pp. 1-5. IEEE, 2023. https://edge.itec.aau.at/wp-content/uploads/sites/15/2023/02/C3-Edge-An-Automated-Mininet-Compatible-SDN-Testbed.pdf 

```
@inproceedings{hammer2023c3,
  title={C3-Edge--An Automated Mininet-Compatible SDN Testbed on Raspberry Pis and Nvidia Jetsons},
  author={Hammer, Josef and Kimovski, Dragi and Mehran, Narges and Prodan, Radu and Hellwagner, Hermann},
  booktitle={NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium},
  pages={1--5},
  year={2023},
  organization={IEEE}
}
```
