import tensorflow as tf 
from PIL import Image
import numpy as np
mnist = tf.keras.datasets.mnist
from keras.preprocessing.image import *
from grapher import grapher 


model = tf.keras.models.load_model('my_model.h5')


class getText:
    def __init__(self, img_lst):
        self.img_lst = img_lst
    def return_text(self):
        for img in self.img_lst:
            img_f= Image.open(img)

            img_f = img_f.resize((28,28))
            img_arr = np.array(img_f)  
            img_arr = img_arr/255.0
            img_arr = img_arr.reshape((1, 28, 28))
            #grapher(img_arr).visualizeGraph()

            predictions = model.predict(img_arr)
            predicted_number = np.argmax(predictions )
            print(predicted_number)
            