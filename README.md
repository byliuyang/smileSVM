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
     pcost       dcost       gap    pres   dres
 0:  2.5000e-01  2.1908e+00  1e+01  2e+00  8e+00
 1:  1.6727e+00  6.8840e-01  1e+00  4e-16  8e-15
 2:  1.0290e+00  9.5474e-01  7e-02  4e-16  3e-15
 3:  1.0035e+00  9.9611e-01  7e-03  5e-16  1e-13
 4:  1.0005e+00  9.9950e-01  1e-03  6e-16  2e-13
 5:  1.0001e+00  9.9993e-01  1e-04  0e+00  3e-12
 6:  1.0000e+00  9.9999e-01  2e-05  6e-16  4e-12
 7:  1.0000e+00  1.0000e+00  3e-06  6e-16  1e-11
 8:  1.0000e+00  1.0000e+00  4e-07  5e-16  2e-11
Optimal solution found.
[ 1.00e+00]
[ 1.00e+00]
 -4.000435582252435
[[1. 1.]] [-4.]
Acc=1.0
     pcost       dcost       gap    pres   dres
 0:  6.1173e-01  1.4827e+01  5e+01  2e+00  2e+01
 1:  6.1203e+00  1.3678e+01  3e+01  1e+00  1e+01
 2:  1.0983e+01  3.9242e+01  3e+01  8e-01  9e+00
 3:  3.9222e+01  7.9561e+01  3e+01  5e-01  5e+00
 4:  8.2069e+01  8.9152e+01  8e+00  9e-02  9e-01
 5:  9.0865e+01  9.0958e+01  1e-01  1e-03  1e-02
 6:  9.0983e+01  9.0984e+01  1e-03  1e-05  1e-04
 7:  9.0984e+01  9.0984e+01  1e-05  1e-07  1e-06
 8:  9.0984e+01  9.0984e+01  1e-07  1e-09  1e-08
Optimal solution found.
[17.45427627]
Acc=1.0
```

## Authors

- **Ben Hylak** - *Initial work* - [bhylak](https://github.com/bhylak)

- **Yang Liu** - *Initial work* - [byliuyang](https://github.com/byliuyang)

## License
This repo is maintained under MIT license.