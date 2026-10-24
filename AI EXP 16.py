
from sklearn.tree import DecisionTreeClassifier

X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = ['Yes', 'Yes', 'No', 'No']

model = DecisionTreeClassifier()
model.fit(X, y)

print("Decision Tree Prediction:")
print(model.predict([[1, 1]]))
print(model.predict([[0, 0]]))
