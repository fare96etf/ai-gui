from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

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
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # define the keras model
    model = Sequential()
    
    first_layer = layers[0]
    model.add(Dense(first_layer["neurons"], input_shape=(col_no-len(outputs),), activation=first_layer["activation"]))
    
    for layer in layers[1:]:
        model.add(Dense(layer["neurons"], activation=layer["activation"]))
    
    # compile the keras model
    model.compile(loss=compile_params["loss"], optimizer=compile_params["optimizer"], metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X_train, y_train, epochs=fit_params["epochs"], batch_size=fit_params["batch_size"], verbose=0)
    # make class predictions with the model
    predictions = (model.predict(X))
    # summarize the first 5 cases
    for i in range(5):
        print(X[i], end="")
        print(" => ", end="")
        print(predictions[i], end="")
        print(" (expected ", end="")
        print(y[i], end="")
        print(")")
    print("TRAINING COMPLETED")
    
    # evaluate
    evaluation = model.evaluate(X_test, y_test)
    
    return evaluation
