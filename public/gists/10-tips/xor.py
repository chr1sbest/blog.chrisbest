array = [1, 2, 4, 8]

if 4 in array:
    pass        # True. This will execute.

if array[0] == 1:
    pass        # True. This will execute.

if bool(4 in array) != bool(array[0] == 1):
    pass        # (True != True) is False. This will not execute!
