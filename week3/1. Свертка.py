import numpy as np
import scipy.signal

image = np.array([[0, -8, -3, -2], [1, 9, -8, 0], [9, -4, 5, -9], [6, -4, 6, 3]])
kernel = np.array([[4, -5, 4], [-6, -8, -2], [1, 5, 5]])

result = scipy.signal.convolve2d(image, kernel, mode='valid')
print(result)
