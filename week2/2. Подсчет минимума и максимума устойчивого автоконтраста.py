from skimage.io import imread, imsave

img = imread('img.png')

pixels = []
for row in img:
    for pixel in row:
        pixels.append(pixel)
pixels.sort()

k = round(len(pixels) * 0.05)

print(pixels[k], pixels[-k])
