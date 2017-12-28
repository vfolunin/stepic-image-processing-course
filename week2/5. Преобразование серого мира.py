from skimage.io import imread, imsave
from skimage import img_as_float
from numpy import clip, dstack, average

img = imread('img.png')
img_f = img_as_float(img)

r = img_f[:, :, 0]
g = img_f[:, :, 1]
b = img_f[:, :, 2]

ra = average(r)
ga = average(g)
ba = average(b)
a = (ra + ga + ba) / 3
ra /= a
ga /= a
ba /= a

r /= ra
g /= ga
b /= ba

img = dstack((r, g, b))
img = clip(img, 0, 1)

imsave('out_img.png', img)
