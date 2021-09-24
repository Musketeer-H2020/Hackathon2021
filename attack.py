# -*- coding: utf-8 -*-
'''
This file contains the abstract class to implement an attack and also two instances that must be implemented by the participants:

- ImplementedAttack1

- ImplementedAttack2

This attack will be used by two workers in the hackathon, the goal is to reduce the accuracy in a scenario where 8 workers are honest and 2 workers are malicious.

'''

__author__ = "Roberto Díaz Morales"
__date__ = "September 2021"


import numpy as np
from abc import ABCMeta, abstractmethod




class Attack(object, metaclass=ABCMeta):
    """
    This class conains two methods, preprocess and process that can be used to implement an attack, they run in a worker node.
    """

    @abstractmethod
    def preprocess(self, Xtr_b, ytr):
        """
        This function is called once, before the training process starts.

        It can be used to make changes on the local dataset that will remain along the training process and also to compute statistics based on the local training set
        instead of perform these computations in every iteration of the training process. It can be also used to create atributes for the object instantiated with this class.

        Parameters
        ----------
        Xtr_b: numpy array
            A numpy matrix where every row is a sample and every column a feature.

        ytr: numpy array
            The class of every data sample in a one hot encoding format:

            [[1 0 0 0]    -> The first sample belongs to class 1
            [0 0 1 0]     -> The first sample belongs to class 3
            [0 1 0 0]     -> The first sample belongs to class 2
            [0 1 0 0]]    -> The first sample belongs to class 2
 

        Returns
        ----------
        Xtr_final: numpy array
            A numpy matrix where every row is a sample and every column a feature. This matrix will be used in the training process

        ytr_final: numpy array
            The label of every data sample in a one hot encoding format, this labels will be used in the training process:

            [[1 0 0 0]    -> The first sample belongs to class 1
            [0 0 1 0]     -> The first sample belongs to class 3
            [0 1 0 0]     -> The first sample belongs to class 2
            [0 1 0 0]]    -> The first sample belongs to class 2

        """
        pass

 
    @abstractmethod
    def process(self, model, weights, Xtr_b, ytr, epochs, batch_size):

        """
        This function receives a neural network, the training set and the number of epochs and batch size requested by the master node. It trains the neural network. 

        Parameters
        ----------
        model: Keras model
            The neural network used in the local training process

        weights: list of numpy arrays
            The weights received by the master node that will be used to initializate the neural network.

        Xtr_b: numpy array
            The local training set. A numpy matrix where every row is a sample and every column a feature.

        ytr: numpy array
            The labels of the local training set. The class of every data sample in a one hot encoding format.

        epochs: int
            Number of training epochs requested by the master node.

        batch_size: int
            The batch size requested by the master node to be used during training.


        """
        pass


class ImplementedAttack1(Attack):

    """
    This class implements the Stocastic Gradient Descent optimization approach, run at Master node. It inherits from :class:`GradientOptimizer`.
    """

    def __init__(self):
        """
        Create a :class:`ImplementedAttack1` instance.

        """


    def preprocess(self, Xtr_b, ytr):
        """
        This function is called once, before the training process starts.

        It can be used to make changes on the local dataset that will remain along the training process and also to compute statistics based on the local training set
        instead of perform these computations in every iteration of the training process. It can be also used to create atributes for the object instantiated with this class.

        Parameters
        ----------
        Xtr_b: numpy array
            A numpy matrix where every row is a sample and every column a feature.

        ytr: numpy array
            The class of every data sample in a one hot encoding format:

            [[1 0 0 0]    -> The first sample belongs to class 1
            [0 0 1 0]     -> The first sample belongs to class 3
            [0 1 0 0]     -> The first sample belongs to class 2
            [0 1 0 0]]    -> The first sample belongs to class 2
 

        Returns
        ----------
        Xtr_final: numpy array
            A numpy matrix where every row is a sample and every column a feature. This matrix will be used in the training process

        ytr_final: numpy array
            The label of every data sample in a one hot encoding format, this labels will be used in the training process:

            [[1 0 0 0]    -> The first sample belongs to class 1
            [0 0 1 0]     -> The first sample belongs to class 3
            [0 1 0 0]     -> The first sample belongs to class 2
            [0 1 0 0]]    -> The first sample belongs to class 2

        """

        ########################################
        # TO BE MODIFIED BY THE PARTICIPANTS
        Xtr_final = Xtr_b.copy()  # This is an example with no attack, the dataset is not modified
        ytr_final = ytr.copy()    # This is an example with no attack, the labels are not modified
        #########################################

        return Xtr_final,ytr_final

    def process(self, model, weights, Xtr_b, ytr, epochs, batch_size):

        """
        This function receives a neural network, the training set and the number of epochs and batch size requested by the master node. It trains the neural network. 

        Parameters
        ----------
        model: Keras model
            The neural network used in the local training process

        weights: list of numpy arrays
            The weights received by the master node that will be used to initializate the neural network.

        Xtr_b: numpy array
            The local training set. A numpy matrix where every row is a sample and every column a feature.

        ytr: numpy array
            The labels of the local training set. The class of every data sample in a one hot encoding format.

        epochs: int
            Number of training epochs requested by the master node.

        batch_size: int
            The batch size requested by the master node to be used during training.


        """

        ########################################
        # TO BE MODIFIED BY THE PARTICIPANTS
        model.keras_model.set_weights(weights)                                                # This is an example with no attack, first we load the weights in the neural network.
        model.keras_model.fit(Xtr_b, ytr, epochs=epochs, batch_size=batch_size, verbose=1)    # This is an example with no attack, we just train the neural network.
        #########################################


class ImplementedAttack2(Attack):

    """
    This class implements the Stocastic Gradient Descent optimization approach, run at Master node. It inherits from :class:`GradientOptimizer`.
    """

    def __init__(self):
        """
        Create a :class:`ImplementedAttack2` instance.

        """


    def preprocess(self, Xtr_b, ytr):
        """
        This function is called once, before the training process starts.

        It can be used to make changes on the local dataset that will remain along the training process and also to compute statistics based on the local training set
        instead of perform these computations in every iteration of the training process. It can be also used to create atributes for the object instantiated with this class.

        Parameters
        ----------
        Xtr_b: numpy array
            A numpy matrix where every row is a sample and every column a feature.

        ytr: numpy array
            The class of every data sample in a one hot encoding format:

            [[1 0 0 0]    -> The first sample belongs to class 1
            [0 0 1 0]     -> The first sample belongs to class 3
            [0 1 0 0]     -> The first sample belongs to class 2
            [0 1 0 0]]    -> The first sample belongs to class 2
 

        Returns
        ----------
        Xtr_final: numpy array
            A numpy matrix where every row is a sample and every column a feature. This matrix will be used in the training process

        ytr_final: numpy array
            The label of every data sample in a one hot encoding format, this labels will be used in the training process:

            [[1 0 0 0]    -> The first sample belongs to class 1
            [0 0 1 0]     -> The first sample belongs to class 3
            [0 1 0 0]     -> The first sample belongs to class 2
            [0 1 0 0]]    -> The first sample belongs to class 2

        """
        ########################################
        # TO BE MODIFIED BY THE PARTICIPANTS
        Xtr_final = Xtr_b.copy()  # This is an example with no attack, the dataset is not modified
        ytr_final = ytr.copy()    # This is an example with no attack, the labels are not modified
        #########################################

        return Xtr_final,ytr_final


    def process(self, model, weights, Xtr_b, ytr, epochs, batch_size):

        """
        This function receives a neural network, the training set and the number of epochs and batch size requested by the master node. It trains the neural network. 

        Parameters
        ----------
        model: Keras model
            The neural network used in the local training process

        weights: list of numpy arrays
            The weights received by the master node that will be used to initializate the neural network.

        Xtr_b: numpy array
            The local training set. A numpy matrix where every row is a sample and every column a feature.

        ytr: numpy array
            The labels of the local training set. The class of every data sample in a one hot encoding format.

        epochs: int
            Number of training epochs requested by the master node.

        batch_size: int
            The batch size requested by the master node to be used during training.


        """
        ########################################
        # TO BE MODIFIED BY THE PARTICIPANTS
        model.keras_model.set_weights(weights)                                                # This is an example with no attack, first we load the weights in the neural network.
        model.keras_model.fit(Xtr_b, ytr, epochs=epochs, batch_size=batch_size, verbose=1)    # This is an example with no attack, we just train the neural network.
        #########################################


