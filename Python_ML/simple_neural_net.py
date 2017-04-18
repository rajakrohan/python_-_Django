import numpy as np
import pandas as pd
import math


def train(trainX, trainY):

    X = modifyX(trainX)

    m = X.shape[0]
    pi = X.shape[1]
    po = 3

    np.random.seed(1)

    k = 20
    #Dimension of hidden layer: m * k
    W0 = np.random.rand(pi,k)
    W1 = np.random.rand(k, po)

    a0 = X
    y = np.zeros((m,3))
    for i in range(m):
        y[i,trainY[i]] = 1

    #hyperparameters
    step_size = 2.5
    num_iterations =2000

    for i in range(num_iterations):
        a1, a2 = forward_propagation(a0, W0, W1)
        
        #Calculation of loss
        if i % 10 == 0:
            loss = cross_entropy_error(a2,y)
            print "iteration %d: loss %f" % (i, loss)
        
        W0, W1 = back_prop(a0, a1, a2, W0, W1, y, step_size)        

    np.savez('weights.npz', a=W0, b=W1)

def test(testX):
    data = np.load('weights.npz')
    X = modifyX(testX)
    W0 = data['a']
    W1 = data['b']
    a0 = X
    a1, a2 = forward_propagation(a0, W0, W1)
    return np.argmax(a2, axis = 1)

def sigmoid(x, deriv = False):
    if deriv == True:
        return x*(1-x)
    return 1/(1 + np.exp(-x))

def softmax(x):
    x = x.T
    x=x.astype(float)
    result=np.zeros_like(x)
    M,N=x.shape
    for n in range(N):
        S=np.sum(np.exp(x[:,n]))
        result[:,n]=np.exp(x[:,n])/S
    result = result.T
    return result

def cross_entropy_error(a2, y):
    s = 0
    for i in range(a2.shape[0]):
        for j in range(a2.shape[1]):
            s += -1* y[i][j] * math.log(a2[i][j])
    return s

def modifyX(trainX):
    X = np.reshape(trainX, (trainX.shape[0], -1))
    #X = np.insert(X, 0, 1, 1)
    X['1'] = 1
    return X

def forward_propagation(a0, W0, W1):
    x1 = np.dot(a0, W0)
    a1 = sigmoid(x1)

    x2 = np.dot(a1, W1)
    a2 = softmax(x2)

    return a1, a2

def back_prop(a0, a1, a2, W0, W1, y, step_size):
    #Gradient on scores
    delta_2 = a2 - y
    delta_2 /= y.shape[0]
    dW1 = np.dot(a1.T, delta_2)
    delta_1 = np.dot(delta_2, W1.T)
    da = sigmoid(a1, deriv = True)
    delta_1 *= da
    dW0 = np.dot(a0.T, delta_1)
    W0 += -step_size*dW0
    W1 += -step_size*dW1
    return W0, W1

def load_mnist():
    trX = pd.read_csv('trX.txt')
    trX = trX.drop('ID',axis=1)
    trY = pd.read_csv('trY.txt')
    trY['X8'] = trY['X8'] - 1
    trY = trY.drop('ID',axis=1)
    teX = trX
    teY = trY
    trY = np.asarray(trY)
    print trY.shape

    print trX.shape , trY.shape , teX.shape , teY.shape
    return trX, trY, teX, teY


def main():
    trainX, trainY, testX, testY = load_mnist()
    print "Shapes: ", trainX.shape, trainY.shape, testX.shape, testY.shape

    train(trainX, trainY)
    labels = test(testX)
    testY = np.matrix(testY).T #Added this line myself
    accuracy = np.mean((labels == testY)) * 100.0
    print "\nIN MAIN : Test accuracy: %lf%%" % accuracy


if __name__ == '__main__':
    main()
    
