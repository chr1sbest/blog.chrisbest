# Swapping elements
array = ['first', 'second', 'third']
tmp = array[0]
array[0] = array[2]
array[2] = tmp

# Single line element swap
array[0], array[2] = array[2], array[0]
