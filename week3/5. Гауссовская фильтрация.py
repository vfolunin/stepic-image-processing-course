import math
from skimage.io import imread, imsave
from numpy import ndarray, clip


def gauss(sigma, x, y):
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))


def gauss_kernel(sigma):
    k = 2 * round(3 * sigma) + 1
    kernel = ndarray(shape=(k, k), dtype=float)
    for i in range(k):
        for j in range(k):
            kernel[i, j] = gauss(sigma, j - k // 2, i - k // 2)
    return kernel / kernel.sum()


def apply_kernel(img, kernel):
    k = kernel.shape[0]
    res = ndarray(shape=(img.shape[0] - k // 2 * 2, img.shape[1] - k // 2 * 2), dtype=int)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i, j] = int((img[i:i + k, j:j + k] * kernel).sum())
    return clip(res, 0, 255)


img = imread('img.png')
kernel = gauss_kernel(0.66)
res_img = apply_kernel(img, kernel)

imsave("out_img.png", res_img)

