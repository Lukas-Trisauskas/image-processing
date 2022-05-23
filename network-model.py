import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Dropout, Flatten, Activation

from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.models import load_model
from sklearn.metrics import confusion_matrix
import itertools

import os, shutil, random, glob, matplotlib.pyplot as plt, numpy as np

labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
validation_percent = 0.1
batch_size = 50
target_size = (96, 96)
target_dims = (96, 96, 3) # add channel for RGB
n_classes = 26
epoch = 10
data_dir = 'asl_alphabet_train'
test_data_dir = 'asl_alphabet_test'
data_augmentor = ImageDataGenerator(samplewise_center=True, 
                                    samplewise_std_normalization=True, 
                                    validation_split=validation_percent)

# physical_devices = tf.config.experimental.list_physical_devices('GPU')
# print(len(physical_devices))
# if len(physical_devices):
#     tf.config.experimental.set_memory_growth(physical_devices[0],True)
#     print("using GPU"+ str(physical_devices[0]) + "to train")
# else:
#     print("using CPU to train")

def plotImages(images):
    fig, axes = plt.subplots(8,8,figsize=(96,96))
    axes = axes.flatten()
    for img, ax in zip(images, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()
  
def plot_confusion_matrix(cm, classes,normalize=False, title="Confusion Matrix", cmap=plt.cm.Blues):
    plt.imshow(cm,interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks,classes,rotation=45)
    plt.yticks(tick_marks,classes)
    thresh =cm.max()/2.
    for i,j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j,i,cm[i,j],horizontalalignment="center",color="white" if cm[i,j]>thresh else "black")
    plt.tight_layout()
    plt.ylabel("True")
    plt.xlabel("Pred")


def expandTestSet(numToExpand):
    for label in labels:
        for c in random.sample(glob.glob('asl_alphabet_train/'+label+'/*'),numToExpand):
            shutil.move(c, 'asl_alphabet_test/'+label)

train_generator = data_augmentor.flow_from_directory(data_dir, target_size=target_size, batch_size=batch_size, subset="training") 
val_generator = data_augmentor.flow_from_directory(data_dir, target_size=target_size, batch_size=batch_size, subset="validation")

my_model = Sequential()
my_model.add(Conv2D(64, kernel_size=4, strides=1, activation='relu', input_shape=target_dims))
my_model.add(Conv2D(64, kernel_size=4, strides=2, activation='relu'))
my_model.add(Dropout(0.5))
my_model.add(Conv2D(128, kernel_size=4, strides=1, activation='relu'))
my_model.add(Conv2D(128, kernel_size=4, strides=2, activation='relu'))
my_model.add(Dropout(0.5))
my_model.add(Conv2D(256, kernel_size=4, strides=1, activation='relu'))
my_model.add(Conv2D(256, kernel_size=4, strides=2, activation='relu'))
my_model.add(Flatten())
my_model.add(Dropout(0.5))
my_model.add(Dense(512, activation='relu'))
my_model.add(Dense(n_classes, activation='softmax'))


my_model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=["accuracy"])
my_model.fit(x=train_generator, validation_data=val_generator, shuffle=True, epochs=epoch, verbose=1)

my_model.save('asl_model.h5')