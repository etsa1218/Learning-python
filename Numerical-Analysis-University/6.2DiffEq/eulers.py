
# main funkshin
def euler(initialx, endx, initialy, f, step):
    if (endx - initialx) / step != int((endx - initialx) / step):
        return ValueError("Step must divide evenly in the interval")
    x = initialx
    y = initialy

    while x < endx:
        y = y + (step * f(x, y))
        x = x + step
    return y
