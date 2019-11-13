from sklearn.metrics import accuracy_score,r2_score
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris,load_diabetes

# Load dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Training and test matrices, training and test vectors
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Regression
model = neighbors.KNeighborsRegressor()


model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = r2_score(y_test, predictions)
print(f"KNN Accuracy: {accuracy}")

