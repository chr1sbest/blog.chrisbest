# Superheroes in a foot race!
race_results = ['Flash', 'Superman', 'Batman', 'Aquaman']

# [index] (wraps all the way around with negative values)
slowest = race_results[-1]      # 'Aquaman'

# [begin:end] (can omit either or both)
all_racers = race_results[:]    # ['Flash', 'Superman', 'Batman', 'Aquaman']
first_three = race_results[:2]  # ['Flash', 'Superman', 'Batman']
last_two = race_results[-2:]    # ['Batman', 'Aquaman']

# [begin:end:step]
reversed = race_results[::-1]   # ['Aquaman', 'Batman', 'Superman', 'Flash']
every_other = race_results[::2] # ['Aquaman', Superman']
