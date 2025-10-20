from functools import reduce
from multiprocessing import Pool

list = [str(i) for i in range(1, 10000)]

def square_if_valid(x):
    return int(x)**2 if '#' not in x else 0

def sum_of_squares_mp(l):
    with Pool() as pool:
        squared_values = pool.map(square_if_valid, l)
    return sum(squared_values)