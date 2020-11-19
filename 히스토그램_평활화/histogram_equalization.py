import cv2
import numpy as np

img = cv2.imread('dgu_night.png', 0)  # input image
height, width = img.shape
result = np.zeros((height, width), np.uint8)  # result image
size = height * width  # image size

# calculate input image's histogram
histogram = np.zeros(256)
for y in range(height):
    for x in range(width):
        value = img[y, x]
        histogram[value] += 1

# calculate input image's cumulative histogram
cumulative_histogram = np.zeros(256)
sum = 0
for i in range(256):
    sum += histogram[i]
    cumulative_histogram[i] = sum

# normalized cumulative histogram
normalized_cumulative_histogram = np.zeros(256)
for i in range(256):
    normalized_cumulative_histogram[i] = cumulative_histogram[i] / size

# make result image
for y in range(height):
    for x in range(width):
        result[y, x] = normalized_cumulative_histogram[img[y, x]] * 255

cv2.imshow('result', result)
cv2.imwrite('result.png', result)  # save result img
cv2.waitKey(0)
cv2.destroyAllWindows()
