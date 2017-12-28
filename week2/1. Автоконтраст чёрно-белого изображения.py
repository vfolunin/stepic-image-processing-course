from skimage.io import imread, imsave
from numpy import amin, amax

img = imread('img.png')
mn, mx = amin(img), amax(img)

img = (img - mn) / (mx - mn) * 255
img = img.astype('uint8')

imsave('out_img.png', img)

