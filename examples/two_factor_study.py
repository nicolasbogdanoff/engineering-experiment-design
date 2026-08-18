import numpy as np

from engineering_experiment_design import estimate_effects, full_factorial

names, design = full_factorial(["temperature", "feed_rate"])
response = 42 + 4 * design[:, 0] - 1.5 * design[:, 1] + np.array([0.2, -0.1, 0.1, -0.2])
coefficients = estimate_effects(design, response)

print("Runs:")
for row, value in zip(design, response):
    print(dict(zip(names, row)), f"response={value:.2f}")
print("Intercept and coded main effects:", coefficients)
