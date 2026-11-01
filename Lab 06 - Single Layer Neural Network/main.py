"""Train a single sigmoid neuron to classify the AND truth table."""

from math import exp


def sigmoid(value):
    if value >= 0:
        return 1.0 / (1.0 + exp(-value))
    exponential = exp(value)
    return exponential / (1.0 + exponential)


def main():
    features = [[0, 0], [0, 1], [1, 0], [1, 1]]
    labels = [0, 0, 0, 1]
    weights = [0.0, 0.0]
    bias = 0.0
    learning_rate = 0.5
    iterations = 10000

    for _ in range(iterations):
        errors = [
            sigmoid(bias + sum(w * x for w, x in zip(weights, row))) - label
            for row, label in zip(features, labels)
        ]
        bias -= learning_rate * sum(errors) / len(labels)
        weights = [
            weight - learning_rate * sum(error * row[j]
                                         for error, row in zip(errors, features))
            / len(labels)
            for j, weight in enumerate(weights)
        ]

    correct = 0
    print("Input  Expected  Probability  Predicted")
    for row, expected in zip(features, labels):
        probability = sigmoid(bias + sum(w * x for w, x in zip(weights, row)))
        predicted = int(probability >= 0.5)
        correct += predicted == expected
        print(f"{row!s:>7}  {expected:>8}  {probability:>11.4f}  {predicted:>9}")
    print(f"Accuracy: {correct / len(labels) * 100:.1f}%")
    print(f"Learned weights: {[round(weight, 4) for weight in weights]}")
    print(f"Learned bias: {bias:.4f}")


if __name__ == "__main__":
    main()
