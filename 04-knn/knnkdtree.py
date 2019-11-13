from sklearn.datasets import load_iris, load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from classifier import KNNClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KDTree, KNeighborsClassifier

import datetime

starttime = datetime.datetime.now()


def load_data():
    dataset = load_breast_cancer()
    X, y = pd.DataFrame(dataset.data), pd.Series(dataset.target)
    X.columns = dataset.feature_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)
    return y, X_train, X_test, y_train, y_test


def load_data2():
    dataset = load_diabetes()
    X, y = pd.DataFrame(dataset.data), pd.Series(dataset.target)
    X.columns = dataset.feature_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)
    return y, X_train, X_test, y_train, y_test


def main():
    y, X_train, X_test, y_train, y_test = load_data()

    # use kd-tree
    model = KDTree(X_train, metric='euclidean')
    ind = model.query(X_test, k=3, return_distance=False)
    predictions = []
    k_nearest_indexes = ind.tolist()
    for i in k_nearest_indexes:
        counts = np.bincount(np.array(y[i]))
        predictions.append(np.argmax(counts))

    # knn
    model = KNNClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"KNN Accuracy: {accuracy}")


if __name__ == "__main__":
    main()