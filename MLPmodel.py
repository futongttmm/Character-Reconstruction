import numpy as np
import matplotlib.pyplot as plt
from MLP import initialize_parameters_deep, L_model_forward, compute_cost, L_model_backward, update_parameters


def L_layer_model(X, Y, layers_dims, learning_rate = 0.0075, num_iterations = 3000, print_cost=False):
    """
    X -- data -- (num_px * num_px * 3, number of examples)
    Y -- true desired vector, of shape (1, number of examples)
    layers_dims -- list containing the input size and each layer size, of length (number of layers + 1).
    learning_rate -- learning rate of the gradient descent update rule
    num_iterations -- number of iterations of the optimization loop
    print_cost -- if True, it prints the cost every 100 steps

    parameters -- parameters learnt by the model. They can then be used to predict.
    """

    np.random.seed()
    costs = []  # keep track of cost
    
    # Parameters initialization
    parameters = initialize_parameters_deep(layers_dims)
    
    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
        AL, caches = L_model_forward(X, parameters)
        
        # Compute cost.
        cost = compute_cost(AL, Y)
    
        # Backward propagation.
        grads =  L_model_backward(AL, Y, caches)
 
        # Update parameters.
        parameters = update_parameters(parameters, grads, learning_rate)
                
        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))

        costs.append(cost)
            
    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    
    return parameters


def threshold_out (datain):
    dataout = np.zeros(np.shape(datain))
    dataout[:,:] = datain > 0.5
    return dataout.astype(int)


def predict(X, y, parameters):
    """
    X -- data set of examples you would like to label
    parameters -- parameters of the trained model
    p -- predictions for the given dataset X
    """
    
    m = X.shape[1]
    n = len(parameters) // 2 # number of layers in the neural network
    p = np.zeros((X.shape[0],m))
    
    # Forward propagation
    probas, caches = L_model_forward(X, parameters)

    # convert probas to 0/1 predictions
    da = threshold_out(probas)
    
    #print results
    #print ("predictions: " + str(p))
    #print ("true labels: " + str(y))
    # print("Accuracy: "  + str(np.sum((p == y)/m)))
        
    return da