MUSKETEER 2nd Hackathon:
========================

# Attacking federated learning scenarios – Come and try to develop attacks capable of penetrating our defences in a federated learning environment.

## Table of Contents
1. [General Info](#general-info)
2. [Installation](#installation)
2. [Scenarios And Rules](#scenarios-and-rules)
4. [Hackathon Instructions](#hackathon-instructions)
3. [File description](#file-description)

### General Info
***
This repository contains the specific files for the Hackathon2021 organized under the european H2020 project Musketeer (grant agreement No 824988).

![Musketeer logo](https://i2.wp.com/musketeer.eu/wp-content/uploads/2019/02/cropped-MUSKETEER_logo_RGB_2.jpg?w=600&ssl=1)

## Scenarios And Rules
***

We are going to work in a federated learning scenario.

Standard machine learning approaches require centralizing the training data on one machine or in a datacenter. Federated Learning enables different devices to collaboratively learn a shared prediction model while keeping all the training data on device, decoupling the ability to do machine learning from the need to store the data in the cloud. This goes beyond the use of local models that make predictions on mobile devices (like the Mobile Vision API and On-Device Smart Reply) by bringing model training to the device as well.

In this hackathon we have the following elements:

- A master node -> That orchestrate the training
- 10 worker nodes -> Where every worker contains a part of the training set.

The training consists on a model averaging procedure. It is an iterative process:

1. The master node broadcast a neural network to every worker
2. Every worker performs a local training using several epochs the local dataset
3. The workers send back the neural network to the master node, that combines them into a single neural network

This procedure is reapeated several times.

In the hackathon we will test 3 different scenarios:

1. Master node with no defences and two malicious workers.
2. Master node with unknown defence 1 and two malicious workers.
3. Master node with unknown defence 2 and two malicious workers.

The participants must implement the attack of the two malicious workers. This attack must be focused on decreasing the accuracy of the predictive model over the tree scenarios. 


## Installation
***
First, it is neccesary to install the Robust-MMLL repository. 

```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```

## Hackathon Instructions
***

The attacks have to be implemented in the file attack.py that contains two classes (ImplementedAttack1 and ImplementedAttack2). Each one of the two malicious workers will make use of these attacks.

These classes contain two methods to be implemnted:

1. preprocess -> It is executed once at the begining of the training procedure. It receives the local dataset and returns a also a dataset. It can be used to perform modifications over the training dataset that will remain constant along the training procedure.
2. process -> It will be executed every training iteration. It recieves the neural network, the dataset and the training parameters (batch size and number of epochs) and returns the neural network to be sent back to the master node.

## File Description
***
The repository contains the following files:
```
├── data -> This folder contains the training set of every worker and the validation and test sets
│   ├── mnist.test
│   ├── mnist.train.0
│   ├── mnist.train.1
│   ├── mnist.train.2
│   ├── mnist.train.3
│   ├── mnist.train.4
│   ├── mnist.train.5
│   ├── mnist.train.6
│   ├── mnist.train.7
│   ├── mnist.train.8
│   ├── mnist.train.9
│   └── mnist.val
├── README.md -> This file
├── attack.py -> The classes where that participants must implement the attack
├── keras_model_CNN_mnist.json
├── master_hackathon.py -> The code in charge of executing the master node.
├── worker_hackathon.py -> The code in charge of executing a worker node.
├── script_master_and_honest_workers.sh -> A script that run the master and eight worker nodes.
├── script_malicious_workers.sh -> A script that run the workers with the attack implemented in attack.py.
└── README.md```


