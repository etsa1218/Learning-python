def adaptive(f, a, b, tol):

    # trapezoidal rule over whole interval
    Q = (b - a) * (f(a) + f(b)) / 2

    # midpoint
    m = (a + b) / 2

    # trapezoids on left and right halves
    Q_left = (m - a) * (f(a) + f(m)) / 2
    Q_right = (b - m) * (f(m) + f(b)) / 2

    # error estimate
    E = abs(Q - (Q_left + Q_right)) / 3

    # if error too large, split interval
    if E > tol:
        left_val, left_intervals = adaptive(f, a, m, tol/2)
        right_val, right_intervals = adaptive(f, m, b, tol/2)

        # combine results and interval counts
        return left_val + right_val, left_intervals + right_intervals

    else:
        # interval accepted → count as one final interval
        return Q_left + Q_right, 1
