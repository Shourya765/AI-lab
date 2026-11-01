# Lab 01: Linear Regression Using Gradient Descent — From Scratch

## Aim
Implement linear regression with gradient descent from scratch and understand how parameters are updated to minimize the cost function.

## Objectives
- Represent house size and bedroom count as input features.
- Calculate predictions with a linear model.
- Train model parameters using batch gradient descent and mean squared error.
- Use the trained model to predict a house price.

## Algorithm / steps
1. Load the small house-price dataset in `main.py`.
2. Standardize each feature to keep gradient descent stable despite different feature scales.
3. Initialize the bias and feature weights to zero.
4. For each training iteration, calculate predictions and the mean squared error gradients.
5. Update the bias and weights using the learning rate.
6. Print the learned parameters, final cost, and a prediction.

## Source code
See [`main.py`](./main.py). The example data is illustrative; replace it with the data supplied by your instructor if required.

## Run and output
Run `python main.py`. The program prints the final training cost, learned parameters, and predicted price for a sample house. Prices are expressed in thousands of currency units in this example.

## Result and conclusion
The model learns a linear relationship between house size, bedroom count, and price by repeatedly updating its parameters in the direction that reduces mean squared error. Gradient descent performance depends on the data, feature scaling, learning rate, and iteration count.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
