from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def __init__():
    pass

def run_neural_network(data, layers=[], outputs=[]):
    print("TRAINING STARTED")
    # prepare the data
    X = []
    y = []
    
    for column in range(9):
        if column in outputs:
            y.append(list(data[:, column]))
        else:
            X.append(list(data[:, column]))
    
    X = list(map(lambda *el: list(el), *X))
    y = list(map(lambda *el: list(el), *y))
    
    # define the keras model
    model = Sequential()
    model.add(Dense(12, input_shape=(8,), activation='relu'))
    
    for layer in layers:
        model.add(Dense(layer["neurons"], activation=layer["activation"]))
    
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X, y, epochs=150, batch_size=10, verbose=0)
    # make class predictions with the model
    predictions = (model.predict(X) > 0.5).astype(int)
    # summarize the first 5 cases
    for i in range(5):
        print('%s => %d (expected %d)' % (X[i], predictions[i], y[i][0]))
    print("TRAINING COMPLETED")
