# Sorted Search With Conditions

from random import random

values = [random() for i in range(20)]
x = random()

sorted_values = sorted(values)

indices = []
for i in range(len(sorted_values)):
    if sorted_values[i] >= x:
        indices.append(i)

for i in range(len(sorted_values)):
    if sorted_values[i] == x:
        matchingValue = i


print(sorted_values)
print('The value of x is: ' + str(x))
if indices:
    if indices[0] == x:
        print('This is the first index that matches x: ' + str(matchingValue))
    else:
        print('There is no value that matches x.')
else:
    print('There are no values greater than or equal to x.')





