from pil import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Dense, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
import io
import numpy as np
import base64
import tensorflow as tf
from sklearn.externals import joblib
import cv2
cars = [ 'Audi', 'BMW', 'Chevrolet', 'Citroen', 'Volvo']

app = Flask(__name__)

model = joblib.load('model.pkl')

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread('nimg/Audi17708_small.jpg')
img = cv2.resize(img,(50,50))
img = np.reshape(img,[1,50,50,3])

cla = model.predict_classes(img)

print(cla)
    
    
@app.route("/predict", methods=['POST'])
def predict():
    prediction = model.predict_classes(img).tolist()
    response = {
        'prediction': {
             'Audi': 0,
             'BMW': 1,
             'Chevrolet':2,
             'Citroen': 3,
              'volvo': 4
        }
    }
    return jsonify(response)

    #return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False) 
   