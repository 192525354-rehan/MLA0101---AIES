
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Historical medical records
X = [
    [25, 22, 110],
    [45, 30, 150],
    [35, 24, 120],
    [50, 32, 160],
    [28, 21, 100],
    [60, 35, 180],
    [40, 28, 140],
    [55, 33, 170],
    [30, 23, 115],
    [48, 31, 155]
]

# 0 = No disease, 1 = Disease
y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y
)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=3000,
    random_state=1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions) * 100, "%")

# Predict for a new patient
age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
bp = int(input("Enter blood pressure: "))

result = model.predict([[age, bmi, bp]])

if result[0] == 1:
    print("Prediction: Disease")
else:
    print("Prediction: No Disease")
