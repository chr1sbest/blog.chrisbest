from time import time as now

def timed_million_multiply(num):
    start = now()
    multiplied = million_multiply(num)
    end = now()
    ms_delta = (end - start) * 1000     # Milliseconds
    print "Execution time: {0}ms".format(ms_delta)
    return multiplied

def timed_million_divide(num1, num2):
    start = now()
    divided  = million_divide(num1, num2)
    end = now()
    ms_delta = (end - start) * 1000     # Milliseconds
    print "Execution time: {0}ms".format(ms_delta)
    return divided
