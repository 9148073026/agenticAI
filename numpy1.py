import timeit

import numpy as np


def basic_numpy_example():
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    arr3 = np.array([[1, 2], [3, 4], [5, 6]])
    arr4 = np.zeros((2, 3))

    # Basic math operations
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Array 3:\n", arr3)
    print("Array 4 (zeros):\n", arr4)
    print("Addition:", arr1 + arr2)
    print("Multiplication:", arr1 * 2)

    # Matrix example
    matrix = np.array([[1, 2], [3, 4]])
    print("Matrix:\n", matrix)
    print("Matrix transpose:\n", matrix.T)

    # Statistics
    numbers = np.array([10, 20, 30, 40, 50])
    print("Mean:", numbers.mean())
    print("Maximum:", numbers.max())
    print("Minimum:", numbers.min())

    # Slicing
    print("First 3 values:", numbers[:3])
    print("Last 2 values:", numbers[-2:])

    L = range(10000)
    print("Sum of L:", sum(L))
    timing = timeit.timeit("sum(L)", globals={"L": L}, number=1000)
    print("Timeit for sum(L) over 1000 runs:", timing, "seconds")

    a = np.arange(10000)
    print("Sum of a:", np.sum(a))
    timing = timeit.timeit("np.sum(a)", globals={"np": np, "a": a}, number=1000)
    print("Timeit for np.sum(a) over 1000 runs:", timing, "seconds")


if __name__ == "__main__":
    basic_numpy_example()
