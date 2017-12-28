from skimage.io import imread, imshow, imsave
img = imread('img.png')

h, w, c = img.shape
img[h // 2 - 3:h // 2 + 4, w // 2 - 7:w // 2 + 8] = [255, 192, 203]
imsave('out_img.png', img)