## Example of Gradient Descent
This is the example of the [gradient descent](http://en.wikipedia.org/wiki/Gradient_descent) algorithm, which may be used to solve a [linear regression](http://en.wikipedia.org/wiki/Linear_regression) problem.

### Description
This code demonstrates how a gradient descent search may be used to solve the linear regression problem of fitting a line to a set of points. In this problem, we wish to model a set of points using a line. The line model is defined by two parameters - the line's slope `m`, and y-intercept `b`. Gradient descent attemps to find the best values for these parameters, subject to an error function.

The code contains a main function called `run`. This function defines a set of parameters used in the gradient descent algorithm including an initial guess of the line slope and y-intercept, the learning rate to use, and the number of iterations to run gradient descent for.

```python
initial_b = 0 # initial y-intercept guess
initial_m = 0 # initial slope guess
num_iterations = 50
```

Using these parameters a gradient descent search is executed on a sample data set of 100 ponts.

### Execution

The code is running by Python ([version 3.6](https://www.python.org/doc/versions/)).

To run the example, simply run the `gradient_descent.py` file using Python

```
python gradient_descent.py
```

The output will look like this

```
Starting gradient descent at b = 0, m = 0, error = 5565.107834483211
Running...
After 50 iterations b = 0.03207192079925886, m = 1.4788617415595229, error = 112.64886099447925
```