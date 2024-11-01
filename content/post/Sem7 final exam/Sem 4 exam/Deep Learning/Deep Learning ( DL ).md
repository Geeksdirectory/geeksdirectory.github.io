---
title: Deep Learning
categories:
  - exam
  - Sem7
---

![[Pasted image 20241031223620.png]]
![[Pasted image 20241101092507.png]]

---
## Fundamentals of Deep Learning

- Def: Deep Learning is a subset of machine learning that mimics the workings of the human brain to process data and create patterns for decision-making.
- It uses **neural networks** with multiple layers, hence the term "deep."
#### Neural Networks:

- Neural networks are the building blocks of deep learning.
- **Artificial Neural Networks (ANN)** are inspired by biological neural networks and consist of interconnected layers of neurons (nodes).
- Key components of a neural network include **input layers**, **hidden layers**, and **output layers**
#### Layers in Neural Networks:

- **Input Layer**: The first layer that receives input data (e.g., images, text, numerical values).
- **Hidden Layers**: Intermediate layers between input and output layers, where complex computations and transformations happen. Deep networks typically have multiple hidden layers.
- **Output Layer**: Produces the final output (e.g., classification label, predicted value).
#### **Neurons (Nodes)**:

- **Neuron**: The basic unit in a neural network, which computes the weighted sum of inputs, adds a bias term, and passes it through an activation function.
- Each neuron receives input from the previous layer, processes it, and sends output to the next layer.
#### Weights and Biases:

- **Weights**: The strength of the connection between neurons; these are learned during training.
- **Bias**: A constant added to the weighted sum, allowing the model to fit the data more flexibly.

#### Activation function

- Add **non-linearity** to the neural network, enabling it to learn complex patterns.
- Common activation functions:
    - **ReLU (Rectified Linear Unit)**: f(x)=max(0,x)f(x) = max(0, x)f(x)=max(0,x), used to prevent saturation in deep networks.
    - **Sigmoid**: Squashes input values between 0 and 1, useful for binary classification.
    - **Tanh**: Squashes input values between -1 and 1.
    - **Softmax**: Normalizes output into a probability distribution, used in multi-class classification.

#### Feedforward Process:

- In a **feedforward neural network**, data moves forward from the input layer through hidden layers to the output layer.
- Each layer transforms the input data using weights, biases, and activation functions.




















## Multilayered Perceptron ( MLPS )

- A multi-layer perception is a neural network that has multiple layers.
- MLP is a type of [[feedforward]] artificial neural network.
- It consists of at least three layers: an input layer, hidden layer(s), and an output layer.
- To create a neural network we combine neurons together so that the outputs of some neurons are inputs of other neurons.
- It is fully connected dense layers, which transform any input dimension to the desired dimension
- Each connection has an associated weight.
- Neurons have biases, added to the weighted sum before applying the activation.

![[Pasted image 20241101092853.png]]


- Every node in the multi-layer perception uses a [[sigmoid activation]] function
- The sigmoid activation function takes real values as input and converts them to numbers between 0 and 1 using the sigmoid formula.

![[Pasted image 20241101093133.png]]

### Learning process
- Uses backpropagation to update weights based on the error.
- The goal is to minimize a loss function using gradient descent.
### Use cases of MLP
- MLPs are used for tasks like classification, regression, and function approximation.



