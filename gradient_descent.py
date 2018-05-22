import json


# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    total_error = 0
    for i, val in enumerate(points):
        x = val['x']
        y = val['y']
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    n = float(len(points))
    for i, val in enumerate(points):
        x = val['x']
        y = val['y']
        b_gradient += -(2 / n) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / n) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learning_rate)
    return [b, m]


def run():
    file = open('data.json', 'r')
    points = json.load(file)
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept
    initial_m = 0  # initial slope
    num_iterations = 40

    initial_error = compute_error_for_line_given_points(initial_b, initial_m, points)
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, initial_error))

    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    error = compute_error_for_line_given_points(b, m, points)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, error))


if __name__ == '__main__':
    run()
