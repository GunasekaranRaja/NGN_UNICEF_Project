# SKILLSET CLASSIFICATION MODEL

This model involves categorising questions from the dataset using the Small BERTs Model. The model uses smaller transformer blocks compared to the basic BERT model. It allows easy fine-tuning of the model and explores various tradeoffs between speed, size and quality. Dataset consists of questions and the category to which it pertains. The model trains on the given dataset and classifies new questions to their appropriate category.

### Software Prerequisites

- [Python](https://www.python.org/downloads/) 3.6.0+
- [Pytorch](https://pytorch.org/) 1.10.0+
- [Tensorflow](https://www.tensorflow.org/install) 2.0
- [Jupyter Notebook](https://jupyter.org/install) 3.0

### Downloading Prerequisite Packages

Run the following commands to install the additional packages required to run the model:

```bash
pip install transformers
pip install -q -U tensorflow-text
pip install -q tf-models-official
pip install pyyaml h5py
```

### Download, Setup and Run

1. Clone the repository locally. 

```bash
git clone https://github.com/GunasekaranRaja/NGN_UNICEF_Project.git
```

1. Navigate to scripts folder and launch the jupyter notebook via jupyter labs.
2. Run all the cells in the notebook in appropriate order.
