# SKILLSET CLASSIFICATION MODEL

This model involves categorising questions from the dataset using the Small BERTs Model. The model uses smaller transformer blocks compared to the basic BERT model. It allows easy fine-tuning of the model and explores various tradeoffs between speed, size and quality. Dataset consists of questions and the category to which it pertains. The model trains on the given dataset and classifies new questions to their appropriate category.

### Software Prerequisites

- [Python](https://www.python.org/downloads/) 3.7.11
- [Tensorflow](https://www.tensorflow.org/install) 2.5.0
- [Kersas](https://keras.io/) 2.5.0

### Downloading Prerequisite Packages

Run the following commands to install the additional packages required to run the model:

```bash
pip install transformers==4.9.0
pip install -q -U tensorflow-text==2.5.0
pip install -q tf-models-official==2.5.1
pip install pyyaml==5.4.1 h5py==3.1.0
```

### Download, Setup and Run

1. Clone the repository locally. 

```bash
git clone https://github.com/GunasekaranRaja/NGN_UNICEF_Project.git
```

2. Navigate to scripts folder and launch the jupyter notebook via jupyter labs.
3. Run all the cells in the notebook in appropriate order.
