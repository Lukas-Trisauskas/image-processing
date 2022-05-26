import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Activation, Conv2D, Dense, Dropout, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy


batch_size = 50
target_size = (64, 64)
target_dims = (64, 64, 3) # add channel for RGB
n_classes = 26
epoch = 10
validation_percent = 0.1

data_dir = 'asl_alphabet_train'
test_data_dir = 'asl_alphabet_test'

data_generator = ImageDataGenerator(samplewise_center=True, samplewise_std_normalization=True, validation_split=validation_percent)

# creates tensors for training and validation with the split 90/10 
# data held in baches of 50 to lower stress on RAM/CPU/GPU when training 
train_generator = data_generator.flow_from_directory(data_dir, target_size=target_size, batch_size=batch_size, subset="training") 
val_generator = data_generator.flow_from_directory(data_dir, target_size=target_size, batch_size=batch_size, subset="validation")

def createModel():
    # Convolution Neural Network Model used is sequential (group of linear network layers)
        # conv2d is a layer for performung spatial convolution on images
        # dropout prevents overfitting by dropping 0.5 (50%) of the inputs to 0 and scaling remaining inputs accordingly
        # flatten reshapes the inputs in to one value 
        # performs the activation function (relu, softmax) with a bias 
        # modified from https://www.kaggle.com/code/dansbecker/running-kaggle-kernels-with-a-gpu
    model = Sequential()
    model.add(Conv2D(64, kernel_size=4, strides=1, activation='relu', input_shape=target_dims))
    model.add(Conv2D(64, kernel_size=4, strides=2, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Conv2D(128, kernel_size=4, strides=1, activation='relu'))
    model.add(Conv2D(128, kernel_size=4, strides=2, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Conv2D(256, kernel_size=4, strides=1, activation='relu'))
    model.add(Conv2D(256, kernel_size=4, strides=2, activation='relu'))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(n_classes, activation='softmax'))
    return model

def trainModel(model):
    # Trains the model on the train batches
        # compile - configures model for fit function (sets LR, loss funciton and what to evaluate during training)
        # fit - trains a configured model for number of epochs, shuffles the data before each epoch, 
    model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=["accuracy"])
    model.fit(x=train_generator, validation_data=val_generator, shuffle=True, epochs=epoch, verbose=1)

def saveModel(model):
    # Saves model as .h5 file
        # saving with this format includes data such as:
        # weight values
        # compiled model
        # model architecture 
    model.save('asl_model.h5')
