
import numpy as np
from sklearn.neural_network import MLPClassifier

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 1]

model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=5000,
                      random_state=1)
model.fit(X, y)

print("Feed Forward Neural Network")
print("Prediction:", model.predict([[1, 1]]))
