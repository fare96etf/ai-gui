from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def __init__():
    pass

def run_neural_network(data, layers, outputs, compile_params, fit_params):
    print("TRAINING STARTED")
    
    # prepare the data
    X = []
    y = []
    
    col_no = len(data[0])
    
    for column in range(col_no):
        if column in outputs:
            y.append(list(data[:, column]))
        else:
            X.append(list(data[:, column]))
    
    X = list(map(lambda *el: list(el), *X))
    y = list(map(lambda *el: list(el), *y))
    
    # define the keras model
    model = Sequential()
    
    first_layer = layers[0]
    model.add(Dense(first_layer["neurons"], input_shape=(col_no-len(outputs)), activation=first_layer["activation"]))
    
    for layer in layers[1:]:
        model.add(Dense(layer["neurons"], activation=layer["activation"]))
    
    # compile the keras model
    model.compile(loss=compile_params["loss"], optimizer=compile_params["optimizer"], metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X, y, epochs=fit_params["epochs"], batch_size=fit_params["batch_size"], verbose=0)
    # make class predictions with the model
    predictions = (model.predict(X) > 0.5).astype(int)
    # summarize the first 5 cases
    for i in range(5):
        print('%s => %d (expected %d)' % (X[i], predictions[i], y[i][0]))
    print("TRAINING COMPLETED")
