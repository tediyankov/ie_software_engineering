
from functools import reduce

# list
list = [str(i) for i in range(1, 10000)]

# function
def sum_of_squares(l):
    return reduce(lambda x, y: x + y, map(lambda x: int(x)**2 if '#' not in x else 0, l))

# result
print(sum_of_squares(list))