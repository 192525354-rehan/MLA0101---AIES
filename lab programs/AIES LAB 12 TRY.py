
# Decision Tree Classifier

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100, "%")

# User input
sl = float(input("Enter sepal length: "))
sw = float(input("Enter sepal width: "))
pl = float(input("Enter petal length: "))
pw = float(input("Enter petal width: "))

result = model.predict([[sl, sw, pl, pw]])

print("Predicted Flower:", data.target_names[result[0]])
