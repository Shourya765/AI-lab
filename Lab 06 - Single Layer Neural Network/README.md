# Lab 06: Single-Layer Neural Network for Classification

## Aim
Implement a single-layer neural network for binary classification.

## Objectives
- Represent a single neuron with trainable weights and bias.
- Apply a sigmoid activation function.
- Train the network with gradient descent and binary cross-entropy.
- Classify examples and report accuracy.

## Algorithm / steps
1. Prepare feature rows and binary labels for the AND logic-gate dataset.
2. Initialize the neuron's weights and bias.
3. Compute output probabilities using the sigmoid activation.
4. Calculate the output error and update weights and bias using gradient descent.
5. Classify each example at a probability threshold of 0.5 and report results.

## Source code
See [`main.py`](./main.py). A single neuron can learn linearly separable patterns such as AND, but cannot represent XOR.

## Run and output
Run `python main.py`. The output lists the expected and predicted label for each input and the final accuracy.

## Result and conclusion
The single-layer network learns the AND classification rule. Its decision boundary is linear, which limits it to linearly separable data.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
