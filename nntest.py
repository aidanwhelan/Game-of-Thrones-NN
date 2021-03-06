# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:47:11 2018

@author: aidanwhelan
"""

import numpy as np
import matplotlib.pyplot as plt

#Get Training Data
path = '/Users/aidanwhelan/Desktop/GoTTrainingSet.csv'
f = open(path,'r')
count = 0

xarray = np.zeros([199, 5]) #inputs
yarray = np.zeros([199, 1]) #outputs

weightArray1 = np.zeros([5000, 1]) #output weights
weightArray2 = np.zeros([5000, 1]) #output weights
weightArray3 = np.zeros([5000, 1]) #output weights

text = f.readline()
while count < 199:
    text = f.readline()
    if text == '':
        break
    #if 'Column' in text:
     #   print text
    else:
        elements = text.split(',')
        #print len(elements)
        del elements[0:3]
        for i in range(len(elements)):
            if "\r\n" in elements[i]:
                elements[i] = elements[i].replace('\r\n', '')
            elements[i] = float(elements[i])
#        print "Line " + str(count) + ": "
        #print "Elements: "
        #print elements
        xarray[count] = elements[0:5]
        yarray[count] = elements[5]
    count = count+1
 
#Get Testing Data
path = '/Users/aidanwhelan/Desktop/GoTDataSet.csv'
f = open(path,'r')
count = 0

inarray = np.zeros([29, 5])
namearray = []

text2 = f.readline()
while count < 29:
    text2 = f.readline()
    if text2 == '':
        break
    else:
        elements2 = text2.split(',')
        namearray.append(elements2[0])
        del elements2[0:3]
        for i in range(len(elements2)):
            if "\r\n" in elements2[i]:
                elements2[i] = elements2[i].replace('\r\n', '')
            elements2[i] = float(elements2[i])
        #print elements2
        inarray[count] = elements2[0:5]
    count = count + 1

#Input array
X=xarray

#Output
y=yarray

#Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)
#'''
#Variable initialization
epoch=5000 #Setting training iterations
lr=0.0000001 #Setting learning rate
inputlayer_neurons = X.shape[1] #number of features in data set
hiddenlayer_neurons = 3 #number of hidden layers neurons
output_neurons = 1 #number of neurons at output layer

#weight and bias initialization
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))

for i in range(epoch):

#Forward Propogation
    hidden_layer_input1=np.dot(X,wh)
    hidden_layer_input=hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input1=np.dot(hiddenlayer_activations,wout)
    output_layer_input= output_layer_input1+ bout
    output = sigmoid(output_layer_input)

#Back propagation
    E = y-output
    slope_output_layer = derivatives_sigmoid(output)
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) *lr
    
    weightArray1[i] = wout[0]
    weightArray2[i] = wout[1]
    weightArray3[i] = wout[2]
    
    bout += np.sum(d_output, axis=0,keepdims=True) *lr
    wh += X.T.dot(d_hiddenlayer) *lr
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr
print "OUTPUT 1 "
print output

'''

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(activation= 'logistic', solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 3), random_state=1)

print ''
print "Printing fit: "
print clf.fit(X, np.ravel(y))

print "Printing prediction:"
print clf.predict(inarray)
'''
#Forward Pro
hidden_layer_input1=np.dot(inarray,wh)
hidden_layer_input=hidden_layer_input1 + bh
hiddenlayer_activations = sigmoid(hidden_layer_input)
output_layer_input1=np.dot(hiddenlayer_activations,wout)
output_layer_input= output_layer_input1+ bout
output = sigmoid(output_layer_input)

print "OUTPUT 2"
print output

#ANALYZING DATA
minimumIND = 0
minimumVAL = output[0]
for i in range(len(output)):
    if output[i] < minimumVAL:
        minimumIND = i
        minimumVAL = output[i]

print ""
print "Next to die is: "
print namearray[minimumIND]

maxIND = 0
maxVAL = output[0]
for i in range(len(output)):
    if output[i] > maxVAL:
        maxIND = i
        maxVAL = output[i]

print ""
print "Last to die is: "
print namearray[maxIND]

#plt.plot(weightArray1)
#plt.plot(weightArray2)
#plt.plot(weightArray3)
#plt.plot(output)
#plt.show()

