from typing import List, Any, Union
import numpy as np

class Net:
    def __init__(self, shape, activation_function, cost, dcost):
        self.shape = shape
        self.depth = len(shape)
        self.activation_function = activation_function
        self.cost = cost    # cost function
        self.dcost = dcost  # derivative of the cost function

        #create a set of nodes in the given shape
        self.nodes = [np.empty(shape[i]) for i in range(self.depth)]
        self.biases = [np.empty(shape[i]) for i in range(self.depth)]

        # weights run between nodes so there will be one less set of nodes than number of weights
        self.weights = [np.random.rand(shape[i+1], shape[i]) for i in range(self.depth-1)]


    def backprop(self):
        return

    #calculate the activation of a node from a given layer
    def calculate_activation(self, layer):
        self.nodes[layer] = [self.activation_function(self.weights[layer-1][i].dot(self.nodes[layer-1])
                                                      + np.sum(self.biases[layer])) for i in range(self.shape[layer])]

    #calculate the activation for the output by iterating over each layer
    def activation(self):
        for i in range(1, self.depth):
            self.calculate_activation(i)
