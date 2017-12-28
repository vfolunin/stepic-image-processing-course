from skimage.io import imread, imsave
from numpy import array, ndarray, clip


def apply_kernel(img, kernel):
    k = kernel.shape[0]
    res = ndarray(shape=(img.shape[0] - k // 2 * 2, img.shape[1] - k // 2 * 2), dtype=int)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i, j] = int((img[i:i + k, j:j + k] * kernel).sum())
    return clip(res, 0, 255)


img = imread('img.png')
kernel = 0.1 * array([[-1, -2, -1], [-2, 22, -2], [-1, -2, -1]])
res_img = apply_kernel(img, kernel)

imsave("out_img.png", res_img)

