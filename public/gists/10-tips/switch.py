# Typical if/elif/else
if color == 'red':
    print 'firetruck'
elif color == 'blue':
    print 'sky'
elif color == 'yellow':
    print 'sun'
else:
    print 'grey'

# Build a switch object to map arguments->commands
color_switch = {        
 'red': 'firetruck',
 'blue': 'sky',
 'yellow': 'sun'
}
color_switch.get(color, 'grey') # Grey is the default
