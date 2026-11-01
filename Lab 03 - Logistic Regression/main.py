"""Binary logistic regression trained with batch gradient descent."""

from math import exp, sqrt


def sigmoid(value):
    if value >= 0:
        return 1.0 / (1.0 + exp(-value))
    exponential = exp(value)
    return exponential / (1.0 + exponential)


def standardize(features):
    means = [sum(row[j] for row in features) / len(features)
             for j in range(len(features[0]))]
    scales = []
    for j, mean in enumerate(means):
        variance = sum((row[j] - mean) ** 2 for row in features) / len(features)
        scales.append(sqrt(variance) if variance else 1.0)
    scaled = [[(value - means[j]) / scales[j] for j, value in enumerate(row)]
              for row in features]
    return scaled


def train(features, labels, learning_rate=0.1, iterations=3000):
    scaled = standardize(features)
    weights = [0.0] * len(scaled[0])
    bias = 0.0
    count = len(labels)
    for _ in range(iterations):
        errors = [
            sigmoid(bias + sum(w * x for w, x in zip(weights, row))) - label
            for row, label in zip(scaled, labels)
        ]
        bias -= learning_rate * sum(errors) / count
        weights = [
            weight - learning_rate * sum(error * row[j]
                                         for error, row in zip(errors, scaled)) / count
            for j, weight in enumerate(weights)
        ]
    return weights, bias


def main():
    # Features: hours studied and practice tests completed.
    features = [
        [1, 0], [2, 1], [2, 2], [3, 1],
        [5, 3], [6, 4], [7, 4], [8, 5],
    ]
    labels = [0, 0, 0, 0, 1, 1, 1, 1]
    scaled = standardize(features)
    weights, bias = train(features, labels)
    correct = 0
    print("Actual  Predicted  Probability")
    for row, actual in zip(scaled, labels):
        probability = sigmoid(bias + sum(w * x for w, x in zip(weights, row)))
        predicted = int(probability >= 0.5)
        correct += predicted == actual
        print(f"{actual:>6}  {predicted:>9}  {probability:.4f}")
    print(f"Training accuracy: {correct / len(labels) * 100:.1f}%")


if __name__ == "__main__":
    main()
