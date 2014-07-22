# Python's doesn't have a switch case.
# If/elif/else is pretty clean in Python, but its still a hassle.
if color == 'red':
    apply_red()
elif color == 'blue':
    apply_blue()
elif color == 'green':
    apply_green()
elif color == 'orange':
    apply_orange()
elif color == 'purple':
    apply_purple()
elif color == 'yelow':
    apply_yellow()
else:
    do_something_else()

# Build a switch object to map arguments->commands
color_switch = {        
 'red': apply_red       # Functions passed as values
 'blue': apply_blue
 'green': apply_green
 'orange': apply_orange
 'purple': apply_purple
 'yellow': apply_yellow
}

# Only one comparison made. (Is the value at this hashtable address not None?)
if color_switch[color]: 
    color_switch[color]()
else:
    do_something_else

