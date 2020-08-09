---
layout: post
title:  Deep learning using Google Colaboratory
comments: true
categories: [Machine Learning]
excerpt: Deep learning using Google Colaboratory
---

## What to learn here?
- What is neural network and how to train it.
- How to build basic 1-layer neural network using tf.keras
- How to add more layers
- How to setup a learning rate schedule
- How to build convolutional neural network
- How to use regularization techniques: dropout, batch normalization
- What is overfitting?

We will be using Google Collaboratory which requires no setup on your part. To get yourself acquainted with it, visit [Welcome to Colab](https://colab.research.google.com/github/GoogleCloudPlatform/training-data-analyst/blob/master/courses/fast-and-lean-data-science/colab_intro.ipynb)

## Terminology
Some terminologies used in deep learning

**batch** or **mini-batch**: training is always performed on batches of training data and labels. Doing so helps algorithm converge. The 'batch' dimension is typically the first dimention of the data tensors. For example a tensor of shape [100, 192, 192, 3] contains 100 images of 192x192 pixels with 3 values per pixel (RGB)

**cross-entropy loss**: a special loss function often used in classifiers.

**dense layer**: a layer of neurons where each layer is connected to all the neurons in the previous layer.

**features**: the inputs of neural network are sometimes called 'features'. The art of figuring out which part of a dataset (or combination of parts) to feed into a neural network to get good predictions is called 'feature engineering'.

**labels**: another name for *classes* or correct answers in supervised classification problem. 

**learning rate**: fraction of the gradient by which weights and biases are updated at each iteration of the training loop.

**logits**: the outputs of a layer of the neutrons before activation function is applied are called *logits*. The term comes from logistic function a.k.a. the *sigmoid function* which used to the most popular function. *Neuron outputs before logistic function* was shortened to *logits*.

**loss**: the error function comparing neural network outputs to the correct answers.

**neuron**: computes the weighted sum of its inputs, adds a bias and feeds the result through an activation function.

**one-hot encoding**: 

**relu**: rectified linear unit. A popular activation function for neurons.

**sigmoid**: another activation that used to be popular and is still useful in special cases.

**softmax**: a special activation function that acts on a vector, increases the difference between largest component and all others, and also normalizes the vector to have a sum of 1 so that it can be interpreted as vector of probabilities. Used as last step in classifiers.

**tensor**: A *tensor* is like a matrix but with an arbitrary number of dimensions A 1-dimensional tensor is a vector. A 2-dimensional tensor is a matrix. And then you can have tensors of 3,4,5 and more dimensions.

## What is Neural Network?

A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.

Neural networks can adapt to chaning input; so the network generates best possible result without needing to redesign the output criteria.

Six types of Neural Networks currently being used in Machine Learning. For more details [click here](https://analyticsindiamag.com/6-types-of-artificial-neural-networks-currently-being-used-in-todays-technology/)
- Feedforward neural network
- Radial basis function neural network
- Kohonen self organizing neural network
- Recurrent neural network (RNN) - Long short term memory
- Convolutional neural network (CNN)
- Modular neural network



