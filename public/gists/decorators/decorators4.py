from time import time as now

def time_decorator(func):
    """
    Print the amount of milliseconds it took for the function to execute.
    """
    def wrapped(*args, **kwargs):
        start = now()
        result = func(*args, **kwargs)
        end = now()
        ms_delta = (end - start) * 1000
        print "Execution time: {0}ms".format(ms_delta)
        return result
    return wrapped
