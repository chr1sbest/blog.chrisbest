# String formatting
greeting = 'Hello'
name = 'Chris'
age = 23

# Printing via concatenation. Need to be careful with spaces and +'s.
print greeting + ', my name is ' + name + ' and I am ' + str(age) + ' years old.'

# Printing with str.format(). Easier to visualize.
print '{0}, my name is {1} and I am {2} years old.'.format(greeting, name, age)
