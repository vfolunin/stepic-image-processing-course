from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import clip, dstack, roll

img = img_as_float(imread('img.png'))
height = img.shape[0] // 3

b = img[:height, :]
g = img[height:height * 2, :]
r = img[height * 2:height * 3, :]

border_width =  int(img.shape[1] * 0.15)
border_height = int(height * 0.15)
r = r[border_height:-1-border_height, border_width:-1-border_width]
g = g[border_height:-1-border_height, border_width:-1-border_width]
b = b[border_height:-1-border_height, border_width:-1-border_width]

best_correlation = -1
for dy in range(-15, 16):
    for dx in range(-15, 16):
        db = roll(b, dy, axis=0)
        db = roll(db, dx, axis=1)
        correlation = (db * g).sum()
        if best_correlation < correlation:
            best_correlation = correlation
            bdy = dy
            bdx = dx

b = roll(b, bdy, axis=0)
b = roll(b, bdx, axis=1)

best_correlation = -1
for dy in range(-15, 16):
    for dx in range(-15, 16):
        dr = roll(r, dy, axis=0)
        dr = roll(dr, dx, axis=1)
        correlation = (dr * g).sum()
        if best_correlation < correlation:
            best_correlation = correlation
            rdy = dy
            rdx = dx

r = roll(r, rdy, axis=0)
r = roll(r, rdx, axis=1)

imsave('out_img.png', dstack((r, g, b)))

