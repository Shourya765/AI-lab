"""Linear regression for house prices using batch gradient descent."""

from math import sqrt


def standardize_features(features):
    means = [sum(row[column] for row in features) / len(features)
             for column in range(len(features[0]))]
    scales = []
    for column, mean in enumerate(means):
        variance = sum((row[column] - mean) ** 2 for row in features) / len(features)
        scale = sqrt(variance)
        scales.append(scale if scale else 1.0)
    standardized = [
        [(value - means[column]) / scales[column]
         for column, value in enumerate(row)]
        for row in features
    ]
    return standardized, means, scales


def train(features, targets, learning_rate=0.05, iterations=5000):
    scaled_features, means, scales = standardize_features(features)
    weights = [0.0] * len(scaled_features[0])
    bias = 0.0
    sample_count = len(targets)

    for _ in range(iterations):
        predictions = [
            bias + sum(weight * value for weight, value in zip(weights, row))
            for row in scaled_features
        ]
        errors = [prediction - target for prediction, target in zip(predictions, targets)]
        bias_gradient = sum(errors) / sample_count
        weight_gradients = [
            sum(error * row[column] for error, row in zip(errors, scaled_features))
            / sample_count
            for column in range(len(weights))
        ]
        bias -= learning_rate * bias_gradient
        weights = [
            weight - learning_rate * gradient
            for weight, gradient in zip(weights, weight_gradients)
        ]

    final_cost = sum(error ** 2 for error in errors) / (2 * sample_count)
    return weights, bias, means, scales, final_cost


def predict(features, weights, bias, means, scales):
    scaled = [(value - means[i]) / scales[i] for i, value in enumerate(features)]
    return bias + sum(weight * value for weight, value in zip(weights, scaled))


def main():
    # Size in square feet, bedrooms, and price in thousands of currency units.
    features = [
        [900, 2],
        [1200, 2],
        [1500, 3],
        [1800, 3],
        [2200, 4],
        [2600, 4],
    ]
    prices = [180, 220, 285, 320, 390, 450]

    weights, bias, means, scales, cost = train(features, prices)
    sample = [2000, 3]
    estimate = predict(sample, weights, bias, means, scales)

    print(f"Training examples: {len(features)}")
    print(f"Final cost (MSE/2): {cost:.4f}")
    print(f"Learned weights (standardized features): {[round(w, 4) for w in weights]}")
    print(f"Learned bias: {bias:.4f}")
    print(f"Predicted price for {sample[0]} sq ft, {sample[1]} bedrooms: "
          f"{estimate:.2f} thousand")


if __name__ == "__main__":
    main()
