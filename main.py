# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

from mnist import MNIST
import os
import net

training_size, images, labels = 0,0,0
shape = [3,4,5]
neural_net = net.Net(shape, )

def load_data():
    mndata = MNIST(dir_path)
    mndata.gz = True
    images, labels = mndata.load_training()
    training_size = len(images)

def train_data():
    for i in range(training_size):
        ne

def quadratic_cost(expected, output, depth):
    cost = 0.5*sum((expected[i] - output[i])**2 for i in range(len(output)))
    return cost

def sigmoid(x):
    return (math.e**x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
