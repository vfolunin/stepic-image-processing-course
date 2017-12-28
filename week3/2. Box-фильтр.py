from skimage.io import imread, imsave
from numpy import ndarray


def integral_image(img):
    res = ndarray(shape=img.shape, dtype=int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i, j] = img[i, j]
            if i:
                res[i, j] += res[i - 1, j]
            if j:
                res[i, j] += res[i, j - 1]
            if i and j:
                res[i, j] -= res[i - 1, j - 1]
    return res


def pixel_sum(integral_img, i1, j1, i2, j2):
    res = integral_img[i2, j2]
    if i1:
        res -= integral_img[i1 - 1, j2]
    if j1:
        res -= integral_img[i2, j1 - 1]
    if i1 and j1:
        res += integral_img[i1 - 1, j1 - 1]
    return res


img = imread('img.png')
shape = (img.shape[0] - 4, img.shape[1] - 4)

integral_img = integral_image(img)
res_img = ndarray(shape=shape, dtype=int)

for i in range(shape[0]):
    for j in range(shape[1]):
        res_img[i, j] = pixel_sum(integral_img, i, j, i + 4, j + 4) // 25

imsave("out_img.png", res_img)

