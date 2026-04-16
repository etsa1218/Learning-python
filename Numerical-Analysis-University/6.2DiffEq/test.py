from eulers import euler


def f(x, y):
    return (3*x) - (2*y)


result = euler(1, 2, 1, f, 0.5)
print(result)
