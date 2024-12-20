
### 1. **Definition**:
   - Deep learning is a subset of machine learning that uses neural networks with multiple layers to model complex patterns.

### 2. **Neural Network Structure**:
   - Consists of input layer, hidden layers, and output layer.
   - Each neuron performs weighted sum and activation function.

### 3. **Activation Functions**:
   - Sigmoid, ReLU, Tanh, Softmax.
   - Non-linear functions to introduce complexity.

### 4. **Types of Neural Networks**:
   - **Feedforward Neural Networks (FNN)**
   - **Convolutional Neural Networks (CNN)** – Image processing.
   - **Recurrent Neural Networks (RNN)** – Sequential data (e.g., time series).
   - **Generative Adversarial Networks (GANs)** – Data generation.

### 5. **Training**:
   - Uses backpropagation to minimize error.
   - Optimization via gradient descent (SGD, Adam).

### 6. **Loss Functions**:
   - Mean Squared Error (MSE), Cross-Entropy.

### 7. **Overfitting**:
   - Happens when the model learns noise.
   - Mitigated by techniques like dropout, regularization.

### 8. **Batch Normalization**:
   - Normalizes layer inputs, speeding up training and improving stability.

### 9. **Epochs and Batches**:
   - Epoch: One full cycle through training data.
   - Batch: Subset of data for one forward and backward pass.

### 10. **Popular Frameworks**:
   - TensorFlow, PyTorch, Keras.

Good luck with your viva!




### 1. **Perceptron**:
- Used for **binary classification** (e.g., yes/no, true/false).
   - Simplest type of neural network (single-layer).
   - Consists of input nodes, weights, bias, and output node.
   - Activation function (e.g., step function) used for binary classification.

### 2. **Multilayer Perceptron (MLP)**:
   - Extension of perceptron with multiple hidden layers.
   - Fully connected layers.
   - Uses non-linear activation functions (e.g., ReLU, sigmoid).
   - Can solve non-linear problems, unlike single-layer perceptron.

### 1. **Perceptron**:
   - Used for **binary classification** (e.g., yes/no, true/false).

### 2. **Multilayer Perceptron (MLP)**:
   - **Classification** (e.g., image, text).
   - **Regression** (predicting continuous values).
   - **Pattern recognition** (e.g., handwriting, speech).
   - **Function approximation** (learning complex mappings).


### 1. **Sigmoid Activation Function**:
   - **Formula**: $( \sigma(x) = \frac{1}{1 + e^{-x}} )$
   - **Range**: 0 to 1.
   - **Uses**: Binary classification tasks.
	   - **Advantages**: Smooth gradient, interpretable output as probability.
   - **Disadvantages**: Can cause **vanishing gradient problem**; slow convergence for large input values.

### 2. **Tanh (Hyperbolic Tangent) Function**:
   - **Formula**: $\text{tanh}(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ 
   - **Range**: -1 to 1.
   - **Uses**: Classification tasks where negative values are significant.
   - **Advantages**: Centered around zero, stronger gradient than sigmoid.
   - **Disadvantages**: Can also suffer from **vanishing gradient**.

### 3. **ReLU (Rectified Linear Unit)**:
   - **Formula**: $f(x) = \max(0, x)$ 
   - **Range**: 0 to infinity.
   - **Uses**: Most common in hidden layers of deep networks.
   - **Advantages**: Solves vanishing gradient problem, fast computation.
   - **Disadvantages**: Can cause **dying ReLU problem** (neurons stuck inactive for negative inputs).

### 4. **Leaky ReLU**:
$$
   - **Formula**: \( f(x) = x \) if \( x > 0 \), otherwise \( f(x) = 0.01x \).
$$
   - **Range**: Negative to infinity.
   - **Uses**: Variation of ReLU to handle negative inputs.
   - **Advantages**: Prevents dying ReLU problem.
   - **Disadvantages**: Requires tuning of the leak factor.

### 5. **Softmax Function**:
   - **Formula**: \( \sigma(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}} \)
   - **Range**: 0 to 1 (outputs sum to 1).
   - **Uses**: Multi-class classification (probabilities for each class).
   - **Advantages**: Outputs interpretable probabilities.
   - **Disadvantages**: Sensitive to large input values, risk of gradient saturation.

### 6. **Swish**:
   - **Formula**: \( f(x) = x \cdot \sigma(x) \) (where \( \sigma(x) \) is the sigmoid).
   - **Range**: Negative to infinity.
   - **Uses**: Emerging as a smoother alternative to ReLU.
   - **Advantages**: Better gradient flow, smoother transitions.
   - **Disadvantages**: More computationally expensive.