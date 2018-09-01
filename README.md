# Real-Time-Recurrent-Learning


## Introduction


This project utilizes a class of discrete-time Recurrent Neural Networks(RNNs) known as Real Time Recurrent Networks(RTRNs) to obtain the desired response of a dynamic
control system. The system considered is a Multi Input Multi Output(MIMO) system.

## Overview


### Real Time Recurrent Learning(RTRL) v/s Back Propagation Through Time(BPTT)


- In general, vanilla neural networks are known to utilise BPTT as their learning algorithm. In case of RTRNs, the concept of    backpropagation doesn't exist.
That implies The gradient information at t + 1 is  forward  propagated  to  compute  the  gradient  information  at t + 2  and  so  on.   This  is  the  difference. 

- RTRL is a real-time or online technique, whereas BPTT is an offline technique.

- Since it is real time it means the data need not be collected over time from the system and then learn the model.
  The model will be learned as and when the data comes; most of the control problems must be dealt online.
