# smileSVM

## Getting Started

### Prerequisites

- Python 3.6.4

### Installation

To create a virtual environment, go to the project's directory and run:

```
python3 -m virtualenv env
```

To activate the virtual environment, run:

```
source env/bin/activate
```

To install the required python packages, run:

```
pip install -r requirements.txt
```

To leave virtual environment, run:
```
deactivate
```

### Running

To test out the smile classifier, run:

```
python svm.py
```

You should see following output

```
Traceback (most recent call last):
  File "/Users/harryliu/Documents/course_materials/2018-Spring-D/machine-learning/hw4/smileSVM/env/lib/python3.6/site-packages/cvxopt/misc.py", line 1429, in factor
    lapack.potrf(F['S'])
ArithmeticError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/harryliu/Documents/course_materials/2018-Spring-D/machine-learning/hw4/smileSVM/env/lib/python3.6/site-packages/cvxopt/coneprog.py", line 2065, in coneqp
    try: f = kktsolver(W)
  File "/Users/harryliu/Documents/course_materials/2018-Spring-D/machine-learning/hw4/smileSVM/env/lib/python3.6/site-packages/cvxopt/coneprog.py", line 1981, in kktsolver
    return factor(W, P)
  File "/Users/harryliu/Documents/course_materials/2018-Spring-D/machine-learning/hw4/smileSVM/env/lib/python3.6/site-packages/cvxopt/misc.py", line 1444, in factor
    lapack.potrf(F['S'])
ArithmeticError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "svm.py", line 76, in <module>
    test1()
  File "svm.py", line 37, in test1
    svm453X.fit(X, y)
  File "svm.py", line 20, in fit
    sol = solvers.qp(matrix(P, tc='d'), matrix(q, tc='d'), matrix(G, tc='d'), matrix(h, tc='d'))
  File "/Users/harryliu/Documents/course_materials/2018-Spring-D/machine-learning/hw4/smileSVM/env/lib/python3.6/site-packages/cvxopt/coneprog.py", line 4470, in qp
    return coneqp(P, q, G, h, None, A,  b, initvals, kktsolver = kktsolver, options = options)
  File "/Users/harryliu/Documents/course_materials/2018-Spring-D/machine-learning/hw4/smileSVM/env/lib/python3.6/site-packages/cvxopt/coneprog.py", line 2067, in coneqp
    raise ValueError("Rank(A) < p or Rank([P; A; G]) < n")
ValueError: Rank(A) < p or Rank([P; A; G]) < n
```

## Authors

- **Ben Hylak** - *Initial work* - [bhylak](https://github.com/bhylak)

- **Yang Liu** - *Initial work* - [byliuyang](https://github.com/byliuyang)

## License
This repo is maintained under MIT license.