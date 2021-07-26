# SKILLSET CLASSIFICATION MODEL

This model involves categorising questions from the dataset using the Small BERTs Model. The model uses smaller transformer blocks compared to the basic BERT model. It allows easy fine-tuning of the model and explores various tradeoffs between speed, size and quality. Dataset consists of questions and the category to which it pertains. The model trains on the given dataset and classifies new questions to their appropriate category.

### Requirements

Python:3.7.11

Tensorflow:2.5.0

Keras:2.5.0

Transformers :4.9.0

Tensorflow text:2.5.0

Tf-models-officials:2.5.1

Pyyaml: 5.4.1

h5py : 3.1.0


### Download, Setup and Run

1. Clone the repository locally. 

```bash
git clone https://github.com/GunasekaranRaja/NGN_UNICEF_Project.git
```
2. Create a new python virtual environment to avoid conflicts.
3. install requirements
```bash
pip install -r requirements.txt
```
4. Navigate to scripts folder and run the testing script.
