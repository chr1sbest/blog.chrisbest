def memo(func):
    """ Cache results to prevent duplicate calculations. """
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return wrapper

@memo
def fib(n):
    """ Return the nth value in the fibonacci sequence. """
    return n if n < 2 else fib(n-1) + fib(n-2)
