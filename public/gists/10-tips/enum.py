# We want to print the standings alongside the hero names
race_results = ['Flash', 'Superman', 'Batman', 'Aquaman']

# Typically, we would have to iterate using the index
for i in range(len(race_results)):
    print '{0}: {1}'.format(i, race_results[i])

# enumerate() splits the iterable object into (index, value)
# Can use any vars for (index, value), we will use (standing, hero)
for standing, hero in enumerate(race_results): 
    print '{0}: {1}'.format(standing, hero)

