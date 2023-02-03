# Case study


This case study is about video analytics applications.

The Docker images are prepared for the x86 and Arm devices because the testbed located at https://c3.itec.aau.at/.


TABLE: Docker images of video processing business case study.

------------------------------------------------------------
Step      | x86_image              | Arm_image
------------------------------------------------------------

Encoding  | sina88/encoding:amd64  | sina88/encoding:rpi4

Framing   | sina88/framing:amd64   | sina88/framing:rpi4

Training  | sina88/training:amd64  | sina88/lite-training:rpi4

Inference | sina88/inference:amd64 | sina88/inference:rpi4
