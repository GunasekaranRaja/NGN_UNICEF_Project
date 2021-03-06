# -*- coding: utf-8 -*-
"""UNICEF-HF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19qM2rPkS6p6IaJf-f44_1AWf2SvmIOxB
"""

!pip install datasets
!pip install transformers

import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("/content/trainsp.csv")
enc=LabelEncoder()
df.C=enc.fit_transform(df.C)
df.to_csv("/content/trainsp.csv")

import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("/content/test.csv")

df.C=enc.transform(df.C)
df.to_csv("/content/test.csv")

from datasets import load_dataset
tdataset = load_dataset('csv', data_files='/content/trainsp.csv')
tedataset =load_dataset('csv', data_files='/content/test.csv')

tdataset=tdataset.remove_columns("Unnamed: 0")
tedataset=tedataset.remove_columns("Unnamed: 0")
tdataset,tedataset

from transformers import AutoTokenizer

preprocessor_tok = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_function(examples):
    return preprocessor_tok(examples["Q"], padding="max_length", truncation=True)

tokenized_tdatasets = tdataset.map(tokenize_function, batched=True)
tokenized_tedatasets = tedataset.map(tokenize_function, batched=True)

tokenized_tedatasets

import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification

model = TFAutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=6)

small_train_dataset = tokenized_tdatasets["train"].shuffle(seed=42).select(range(136))
small_eval_dataset = tokenized_tedatasets["train"].shuffle(seed=42).select(range(35))

tf_train_dataset = small_train_dataset.remove_columns(["Q"]).with_format("tensorflow")
tf_eval_dataset = small_eval_dataset.remove_columns(["Q"]).with_format("tensorflow")

train_features = {x: tf_train_dataset[x] for x in preprocessor_tok.model_input_names}
train_tf_dataset = tf.data.Dataset.from_tensor_slices((train_features, tf_train_dataset["C"]))
train_tf_dataset = train_tf_dataset.shuffle(len(tf_train_dataset)).batch(2)

eval_features = {x: tf_eval_dataset[x] for x in preprocessor_tok.model_input_names}
eval_tf_dataset = tf.data.Dataset.from_tensor_slices((eval_features, tf_eval_dataset["C"]))
eval_tf_dataset = eval_tf_dataset.batch(2)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=tf.metrics.SparseCategoricalAccuracy(),
)

model.fit(train_tf_dataset, epochs=4)

model.evaluate(eval_tf_dataset)

import numpy as np
inp=preprocessor_tok(' active/passive voice"I forgot my brother running off the train "')
print(inp)
res=model.predict([inp.input_ids])
print(np.argmax(res.logits))
print(res)

enc.classes_

model.save_pretrained("/content/hf_bert_model")

!zip -r /content/hf_trained_model.zip /content/hf_bert_model

