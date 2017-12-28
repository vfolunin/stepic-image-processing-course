from skimage.io import imread, imsave
from numpy import clip

img = imread('img.png')
n, m = img.shape

h = [0] * 256
for i in range(n):
    for j in range(m):
        h[img[i][j]] += 1

cdf = [sum(h[:i + 1]) for i in range(256)]
cdf_min = [x for x in cdf if x > 0][0]

for i in range(n):
    for j in range(m):
        img[i][j] = round((cdf[img[i][j]] - cdf_min) / (n * m - 1) * 255)

img = clip(img, 0, 255)

imsave('out_img.png', img)
