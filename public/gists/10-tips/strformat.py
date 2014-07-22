# String formatting
name = 'Chris'
greeting = 'Hello'
today = 'Monday'

# Printing via concatenation. Need to be careful with spaces and +'s.
print greeting + ', my name is ' + name + ' and today is ' + today + '.'

# Printing with str.format(). Easier to visualize.
print '{0}, my name is {1} and today is {2}.'.format(greeting, name, today)
