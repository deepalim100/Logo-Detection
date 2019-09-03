...#importing libraries
import urllib
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
import urllib
import pickle
import urllib
import cv2
import numpy as np
from flask import Flask, jsonify
import os
import re
import pickle
from sklearn.externals import joblib

# Image processing...
from pil import Image

app = Flask(__name__) 
url="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwj-m4i1-LTkAhXDTX0KHWF9CPEQjRx6BAgBEAQ&url=http%3A%2F%2Fwww.car-brand-names.com%2Fbmw-logo%2F&psig=AOvVaw2RiwYGCDac9q6nBAkkGBQk&ust=1567609959635400"# create a Flask app
def url_to_image(url, resize=50):
  """
  downloads an image from url, converts to numpy array,
  resizes, and returns it
  """
  response = urllib.urlopen(url)
  img = np.asarray(bytearray(response.read()), dtype=np.uint8)
  img = cv2.imdecode(img, cv2.IMREAD_COLOR)
  img = cv2.resize(img, (resize, resize), interpolation=cv2.INTER_CUBIC)
  return img
 
@app.route('/predict/<path:url>', methods=['GET','POST'])
def predict(url):
  img = url_to_image(url) # image array
  ... # here to add some prep steps
  pred = model.predict(img).argmax() # get index of the class with highest prob
  return jsonify({'prediction': label[pred]})

def load_model():
    model = joblib.load('model.pkl')
  #print('initialize model...')
 
  #print 'load weights...'
    model_wt = joblib.load('model_columns.pkl')
  #print 'load label...'
    label = joblib.load('label.pkl')
    return(model,model_wt,label)


if __name__ == '__main__':
    load_model()
    app.run(debug=False) # t
    