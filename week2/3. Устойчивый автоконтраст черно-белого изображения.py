from skimage.io import imread, imsave
from numpy import clip

img = imread('img.png')

pixels = []
for row in img:
    for pixel in row:
        pixels.append(pixel)
pixels.sort()

k = round(len(pixels) * 0.05)
mn, mx = pixels[k], pixels[-k]

img = img.astype('float')
img = (img - mn) / (mx - mn) * 255
img = clip(img, 0, 255)
img = img.astype('uint8')

imsave('out_img.png', img)
