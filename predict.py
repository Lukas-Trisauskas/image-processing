import matplotlib.pyplot as plt, numpy as np, matplotlib.image as mpimg
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import glob
from math import sqrt, ceil

labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
target_size = (64,64)


def loadModel():
    # loads trained network model to predict from
    return load_model("asl_model.h5")

def plotImages(images,result):
    # calculates number of subplots needed and splits evenly through x and y axis
    subplot_size_x = ceil(sqrt(len(images)))
    if subplot_size_x > 5:
        subplot_size_y = ceil(len(images)/5)
        subplot_size_x = 5
    else: 
        subplot_size_y = subplot_size_x
    if subplot_size_y == 1 and subplot_size_x == 1:
        subplot_size_x +=1
    # creates plot (subplots in x, subplots in y, size of subplots)
    fig, axes = plt.subplots(subplot_size_x,subplot_size_y,figsize=(64,64))
    # collapses array into one dimension
    axes = axes.flatten()
    count = 0
    # iterates through images and puts them in next avaliable subplot
    for img, ax in zip(images, axes):
        ax.imshow(img)
        # if the result is a list uses index to set title
        if isinstance(result,list):
            # title of subplot set to the result for corolating image
            ax.set_title(result[count])
            # increment index for result value
            count +=1
        # paramater result is string for one image 
        else:
            ax.set_title(result)
    # hides the decoration surrounding the plots 
    for ax in axes:
        ax.axis('off')
    # displays the plot
    plt.show()

def predictImage(ASL_model, filepath='asl_alphabet_test'):
    data_dir = filepath
    img_for_pred = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=data_dir, target_size=target_size, batch_size=1, shuffle=False)
    predictions = ASL_model.predict(img_for_pred, verbose=0)
    np.round(predictions)
    all_labels = []
    count = 0
    pre_images = []
    all_img_path = []
    for img in glob.glob(data_dir + "/*/*.jpg"):
        pre_images.append(mpimg.imread(img))
        all_img_path.append(img)
    for result in np.argmax(predictions, axis=-1):
        all_labels.append(labels[result])
        count += 1
    return pre_images,all_labels