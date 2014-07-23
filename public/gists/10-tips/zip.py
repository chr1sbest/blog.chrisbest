# I want to combine the following two lists into a list of tuples.
# new_list should look like [(1, 'A'), (2, 'B') ... (5, 'A+')]
student_ids = [1, 2, 3, 4, 5]
grades = ['A', 'B', 'A-', 'C+', 'A+']

# Here is the lame way to do it:
new_list = []
for index in range(len(list1)):
    new_list.append((list1[index], list2[index]))

# Here we use the zip() function:
new_list = zip(list1, list2)

# Example use case:
for student, grade in zip(student_ids, grades):
    print "{0}: {1}".format(student, grade)
