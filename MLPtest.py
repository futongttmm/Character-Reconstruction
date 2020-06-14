import numpy as np
import matplotlib.pyplot as plt
import pickle
from random import randint
from data_am2 import data, desired
from MLPmodel import L_layer_model, predict


def display_image(vec, numrow, numcol):
    result = [[0 for x in range(numcol)] for y in range(numrow)]
    ptr = 0
    for x in range(numrow):
        for y in range(numcol):
            result[x][y]= vec[ptr]
            ptr += 1
    plt.subplot()
    plt.imshow(result, interpolation="nearest")
    plt.show()


def apply_distortion(testdata, numdistortion):
    result = np.copy(testdata)
    veclen = len(result[0])
    for i in range(len(testdata)):
        for j in range(numdistortion):
            p = randint(0, veclen-1)
            if result[i][p] == 0:
                result[i][p] = 1
            else:
                result[i][p] = 0
    return result


x_train = np.asarray(data)
y_train = np.asarray(desired)
x_train = np.transpose(x_train)
y_train = np.transpose(y_train)

layers_dims = (35, 5, 35)

parameters = L_layer_model(x_train, y_train, layers_dims, num_iterations = 10000, print_cost = False)


x_test = np.asarray(data)
# distort = apply_distortion(x_test, 8)
# np.save("distort", distort)
distort = np.load('distort.npy')

print("***********************Distorted Image************************")
for i in range (len(x_test)):
    display_image(distort[i], 7, 5)

x_test = np.asarray(distort)
y_test = np.asarray(desired)
x_test = np.transpose(x_test)
y_test = np.transpose(y_test)

pred_test = predict(x_test, y_test, parameters)

pred_test = np.transpose(pred_test)

print("***********************Recreated Image************************")
for i in range (len(x_test)):
    display_image(pred_test[i], 7, 5)