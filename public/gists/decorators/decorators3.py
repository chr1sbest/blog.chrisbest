@time_decorator             # This is all we need!
def million_multiply(num):
    for i in xrange(0, 1000000):
        num = num * 1.1
    return num

@time_decorator             # Decorator works with any # of parameters!
def million_divide(num1, num2):
    for i in xrange(0, 1000000):
        num = num / num2
    return num
