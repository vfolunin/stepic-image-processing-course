from skimage.io import imread, imshow, imsave
img = imread('img.png')
h, w, c = img.shape

c = img[0, 0]

left = 0
while (img[:, left] == c).all():
    left += 1

up = 0
while (img[up, :] == c).all():
    up += 1

right = 0
while (img[:, -1 - right] == c).all():
    right += 1

down = 0
while (img[-1 - down, :] == c).all():
    down += 1

print(left, up, right, down)

