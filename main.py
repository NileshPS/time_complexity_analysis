#!/bin/python3
import os
import sys
import numpy as np
import timeit
import math
import matplotlib.pyplot as plt
import boost


# Refers either the function using native implementation or the optimized one.
# Set as per the command line argument.
FUNC_INVERSION_COUNT = None
# Length of each test case.
N = np.array([10,   20,   50,   100,  200,  500,  750,   1000,  1500,  2000,  2500,  3000,  3500, 
              4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 15000, 20000, 50000, 75000, 90000, 100000], dtype=np.int64);

# Wrapper function to be passed to timeit.
def wrapper(func, *args, **kwargs):
    def __func__():
        return func(*args, *kwargs)
    return __func__;

def main():
    time_taken = np.zeros( N.size, dtype=np.float64)
    arr = np.array( N.max(), dtype = np.int64)
    j = 0
    for n in N:
        # Generate n random numbers.
        arr = np.zeros(n, dtype=np.int64)
        print("Input size of  %-6d   took " % n, end = '')
        for i in range(0, n):
           arr[i] = np.random.randint(0, (n << 2) + 7)
        routine = wrapper(FUNC_INVERSION_COUNT, arr, n)
        span = timeit.timeit(routine, number = 1)
        print(" %f seconds !" % span)
        time_taken[j] = span
        j += 1
    # Plot the graph.
    plt.xlabel('Input size')
    plt.ylabel('Time Taken')
    plt.plot(N, time_taken)
    # Open a new window for plotting the time complexity function.
    plt.figure()
    plt.xlabel('Input Size')
    plt.ylabel("N^2" if FUNC_INVERSION_COUNT == boost.inversion_count_native else "Nlog2(N)")
    plt.plot(N.copy(), N**2 if FUNC_INVERSION_COUNT == boost.inversion_count_native else N * np.log2(N))
    plt.show()


def help():
    print("Usage : ./main.py ( -n | -o )")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        help()
        sys.exit(1)
    if sys.argv[1] == '-o':
        print("\n\n<---------------- Using Optimized algorithm ----------->\n\n")
        FUNC_INVERSION_COUNT = boost.inversion_count_optimized
    elif sys.argv[1] == '-n':
        print("\n\n<---------------- Using Native algorithm ----------->\n\n")
        FUNC_INVERSION_COUNT = boost.inversion_count_native;
        N = np.extract( N <= 5000, N)
    else:
        print("Unknown argument :-  ", sys.argv[1])
        sys.exit(2)
    main()
    sys.exit(0)
