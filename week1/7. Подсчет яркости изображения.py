from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import clip, dstack

img = imread('img.png')
img_f = img_as_float(img)

r = img_f[:, :, 0]
g = img_f[:, :, 1]
b = img_f[:, :, 2]

imsave('out_img.png', img_as_ubyte(r * 0.2126 + g * 0.7152 + b * 0.0722))
