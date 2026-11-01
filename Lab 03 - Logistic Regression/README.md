# Lab 03: Logistic Regression Using Gradient Descent

## Aim
Implement logistic regression using gradient descent for binary classification.

## Objectives
- Calculate a binary class probability with the sigmoid function.
- Train model weights using the cross-entropy gradient.
- Classify examples using a probability threshold.
- Evaluate the result on a small labeled dataset.

## Algorithm / steps
1. Load feature rows and binary labels.
2. Standardize the features and initialize weights and bias.
3. Calculate predicted probabilities with the sigmoid function.
4. Compute the average gradient of binary cross-entropy and update the parameters.
5. Use a threshold of 0.5 to predict class labels and print the training accuracy.

## Source code
See [`main.py`](./main.py). The small dataset is for demonstration; replace it with your assigned dataset if applicable.

## Run and output
Run `python main.py`. The output includes each example's actual label, predicted label, and probability, followed by accuracy.

## Result and conclusion
Gradient descent adjusts the model weights to reduce binary cross-entropy. Logistic regression estimates class probabilities and separates classes using a chosen decision threshold.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
