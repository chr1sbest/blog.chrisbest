# Make a sublist of ipa's that start with 's'
ipas = ['sierra nevada', 'lagunitas', 'racer five', 'sculpin']

s_ipas = []                                               # Iterative
for beer in ipas:
    if beer.startswith('s'):
        s_ipas.append(beer)

s_ipas = filter(lambda beer: beer.startswith('s'), ipas)  # Lambda
s_ipas = [beer for beer in ipas if beer.startswith('s')]  # List Comprehension
