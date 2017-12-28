from skimage.io import imread, imshow, imsave
img = imread('img.png')
h, w, c = img.shape
img[h // 2][w // 2] = [102, 204, 102]
imsave('out_img.png', img)
