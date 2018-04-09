from cvxopt import solvers, matrix
import numpy as np
import sklearn.svm

class SVM():
    def __init__ (self):
        pass

    # Expects each *row* to be an m-dimensional row vector. X should
    # contain n rows, where n is the number of examples.
    # y should correspondingly be an n-vector of labels (-1 or +1).
    def fit (self, X, y):
        # TODO change these -- they should be matrices or vectors
        n = X.shape[0]
        dimensions = X.shape[1]

        G = make_G(X, y)
        I = np.eye(dimensions)

        P = np.zeros((dimensions + 1, dimensions + 1))

        P[0:dimensions, 0:dimensions] = I[0:dimensions, 0:dimensions]

        q = np.zeros((dimensions + 1, ))

        h = -1 * np.ones((n, ))
        # Solve -- if the variables above are defined correctly, you can call this as-is:
        
        sol = solvers.qp(matrix(P, tc='d'), matrix(q, tc='d'), matrix(G, tc='d'), matrix(h, tc='d'))

        x = sol['x']

        # Fetch the learned hyperplane and bias parameters out of sol['x']
        self.w = x[:-1]  # TODO change this
        self.b = x[-1]  # TODO change this

    # Given a 2-D matrix of examples X, output a vector of predicted class labels
    def predict(self, x):
        return np.sign(x.dot(self.w) + self.b).reshape((x.shape[0], ))

def make_row(h, size):
    return 

def make_G(X, y):
    Y = np.repeat(np.vstack(y), X.shape[1], axis=1)
    return np.hstack((-Y * X, np.reshape(-y, (y.shape[0], 1))))

def test1 ():
    # Set up toy problem
    X = np.array([ [1,1], [2,1], [1,2], [2,3], [1,4], [2,4] ])
    y = np.array([-1,-1,-1,1,1,1])

    # Train your model
    svm = SVM()
    svm.fit(X, y)
    print(svm.w, svm.b)

    # Compare with sklearn
    skLearnSvm = sklearn.svm.SVC(kernel='linear', C=1e15)  # 1e15 -- approximate hard-margin
    skLearnSvm.fit(X, y)
    print(skLearnSvm.coef_, skLearnSvm.intercept_)

    acc = np.mean(svm.predict(X) == skLearnSvm.predict(X))
    print("Acc={}".format(acc))

def test2 ():
    # Generate random data
    X = np.random.rand(20,3)
    # Generate random labels based on a random "ground-truth" hyperplane
    while True:
        w = np.random.rand(3)
        y = 2*(X.dot(w) > 0.5) - 1
        # Keep generating ground-truth hyperplanes until we find one
        # that results in 2 classes
        if len(np.unique(y)) > 1:
            break

    svm = SVM()
    svm.fit(X, y)

    # Compare with sklearn
    skLearnSvm = sklearn.svm.SVC(kernel='linear', C=1e15)  # 1e15 -- approximate hard margin
    skLearnSvm.fit(X, y)
    diff = np.linalg.norm(skLearnSvm.coef_ - svm.w) + np.abs(skLearnSvm.intercept_ - svm.b)
    print(diff)

    acc = np.mean(svm.predict(X) == skLearnSvm.predict(X))
    print("Acc={}".format(acc))

    if acc == 1 and diff < 1e-1:
        print("Passed")

if __name__ == "__main__": 
    test1()
    test2()
