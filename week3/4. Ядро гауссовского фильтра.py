import math
from numpy import ndarray


def gauss(sigma, x, y):
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))


def gauss_kernel(sigma):
    k = 2 * round(3 * sigma) + 1
    kernel = ndarray(shape=(k, k), dtype=float)
    for i in range(k):
        for j in range(k):
            kernel[i, j] = gauss(sigma, j - k // 2, i - k // 2)
    return kernel / kernel.sum()


sigma = float(input())
kernel = gauss_kernel(sigma)
for i in range(kernel.shape[0]):
    for j in range(kernel.shape[1]):
        print('%.5f' % kernel[i, j], end=' ')
    print()
