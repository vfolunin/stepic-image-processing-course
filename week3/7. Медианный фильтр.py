from skimage.io import imread, imsave
from numpy import ndarray, clip


def median_filter(img):
    res = ndarray(shape=(img.shape[0] - 6, img.shape[1] - 6), dtype=int)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i, j] = sorted((img[i:i + 7, j:j + 7]).flatten())[24]
    return res


img = imread('img.png')
res_img = median_filter(img)

imsave("out_img.png", res_img)

