# Typical if/elif/else
if color == 'red':
    print 'firetruck'
elif color == 'blue':
    print 'sky'
elif color == 'yellow':
    print 'sun'
else:
    print 'grey'

# Build a switch object to map arguments -> values
color_switch = {        
 'red': 'firetruck',
 'blue': 'sky',
 'yellow': 'sun'
}
print color_switch.get(color, 'grey') # Grey is the default
