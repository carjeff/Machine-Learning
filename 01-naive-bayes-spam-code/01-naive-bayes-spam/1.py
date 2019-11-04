from sklearn.datasets import load_iris
from sklearn.naive_bayes import MultinomialNB
import sklearn
from sklearn.model_selection import train_test_split

def main():
    # load the data
    iris = load_iris()
    X = iris['data']
    Y = iris['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state= 42)


    MNB = MultinomialNB(alpha= 1.0, fit_prior=True)
    MNB.fit(X_train, Y_train)

    Y_pre = MNB.predict(X_test)
    print(Y_pre)
    print(MNB.score(X_test, Y_test))
main()


