import cv2
import numpy as np
import matplotlib.pyplot as plt

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1)
    print(rotate_matrix)
    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
    return rotated_image

image = cv2.imread('../image/messi.jpg')
rotated_image = rotate_image(image, angle=45)  # Rotate the image by 45 degrees

plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
