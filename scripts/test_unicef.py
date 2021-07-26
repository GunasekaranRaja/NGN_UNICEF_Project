# -*- coding: utf-8 -*-
"""Test_UNICEF.ipynb
"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

!pip install -q tf-models-official

!pip install -q -U tensorflow-text

import os
import shutil

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization  # to create AdamW optimizer

import matplotlib.pyplot as plt

tf.get_logger().setLevel('ERROR')

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard

from datetime import datetime
from packaging import version
from keras.callbacks import TensorBoard
from tensorflow import keras

import tensorboard
tensorboard.__version__

!rm -rf ./logs/

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
!pip install tensorflow-text

from tensorflow import keras
import tensorflow_text
reloaded_model = keras.models.load_model('/content/drive/MyDrive/model23', compile=False)

def print_my_examples(inputs, results):
  result_for_printing = \
    [f'input: {inputs[i]:<30} : class: {results[i][0]:.6f}'
                         for i in range(len(inputs))]
  print(*result_for_printing, sep='\n')
  print()


examples = [
    'How many athletes did Puerto Rico enter in the 1984 Winter Olympics ?',  
    'How many people live in Chile ?',
    'What was the feature list of forbes magazine 2019?',
    'How many cherubs are there on a Trivial Pursuit board ?',
    'What Shakespearean play featured Shylock ?',
    'What magazine paid $5 , 000 for an eight-millimeter film of John F. Kennedys assassination ?'
    'How many stars are there in the sky?'
]


reloaded_results = tf.sigmoid(reloaded_model(tf.constant(examples)))
xnew=[['How many athletes did Puerto Rico enter in the 1984 Winter Olympics ?'], ['How many people live in Chile ?'],['How many cherubs are there on a Trivial Pursuit board ?'], ['What Shakespearean play featured Shylock ?'], ['What magazine paid $5 , 000 for an eight-millimeter film of John F. Kennedys assassination ?']]
ynew = reloaded_model.predict(xnew)

print('Results from the model:')
print_my_examples(examples, reloaded_results)
for i in range(len(xnew)):
	print("X=%s, Predicted=%s" % (xnew[i], ynew[i]))
