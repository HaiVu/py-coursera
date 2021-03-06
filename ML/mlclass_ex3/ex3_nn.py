## Machine Learning Online Class - Exercise 3 | Part 2: Neural Networks

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions
#  in this exericse:
#
#     lrCostFunction.py (logistic regression cost function)
#     oneVsAll.py
#     predictOneVsAll.py
#     predict.py
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#

from numpy import *
from scipy.io import loadmat
from matplotlib.pyplot import *

from displayData import displayData
from predict import predict

## Setup the parameters you will use for this exercise
input_layer_size  = 400   # 20x20 Input Images of Digits
hidden_layer_size = 25    # 25 hidden units
num_labels = 10           # 10 labels, from 1 to 10
                          # (note that we have mapped "0" to label 10)

## =========== Part 1: Loading and Visualizing Data =============
#  We start the exercise by first loading and visualizing the dataset.
#  You will be working with a dataset that contains handwritten digits.
#

# Load Training Data
print 'Loading and Visualizing Data ...'

ex3data1 = loadmat('ex3data1.mat')
X = ex3data1['X']
y = ex3data1['y'].ravel()
m = size(X, 0)

# Randomly select 100 data points to display
sel = random.permutation(m)

fig = figure()
displayData(X[sel[:100], :])
fig.show()

print 'Program paused. Press enter to continue.'
raw_input()

## ================ Part 2: Loading Pameters ================
# In this part of the exercise, we load some pre-initialized
# neural network parameters.

print '\nLoading Saved Neural Network Parameters ...'

# Load the weights into variables Theta1 and Theta2
ex3weights = loadmat('ex3weights.mat')
Theta1 = ex3weights['Theta1']
Theta2 = ex3weights['Theta2']

## ================= Part 3: Implement Predict =================
#  After training the neural network, we would like to use it to predict
#  the labels. You will now implement the "predict" function to use the
#  neural network to predict the labels of the training set. This lets
#  you compute the training set accuracy.

pred = predict(Theta1, Theta2, X)

print '\nTraining Set Accuracy: %f' % (mean(pred == y) * 100)

print 'Program paused. Press enter to continue.'
raw_input()

#  To give you an idea of the network's output, you can also run
#  through the examples one at the a time to see what it is predicting.

#  Randomly permute examples
rp = random.permutation(m)
fig = figure()

for i in rp:
    # Display
    print '\nDisplaying Example Image'
    displayData(column_stack(X[i, :]))
    fig.show()

    pred = predict(Theta1, Theta2, column_stack(X[i,:]))
    print '\nNeural Network Prediction: %d (digit %d)' % (pred, pred % 10)

    # Pause
    print 'Program paused. Press enter to continue, ^C to exit.'
    raw_input()
