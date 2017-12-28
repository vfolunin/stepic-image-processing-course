import math


def gauss(sigma, x, y):
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))


sigma, x, y = [int(_) for _ in input().split()]
print(gauss(sigma, x, y))
