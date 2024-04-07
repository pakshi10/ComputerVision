import numpy as np
import cv2
image_height = 800
image_width = 600
# Create a 100x100 array filled with zeros (black) of type uint8
image = np.zeros((image_height,image_width), dtype=np.uint8)

# Fill the array: if (i+j) is even, set to 0 (black), else set to 255 (white)
for i in range(image_height):
    for j in range(image_width):
        if (i + j) % 2:
            image[i, j] = 255  # White

# Save the image to the current directory
cv2.imwrite('../images/alternatepixels.png', image)
#Zoom the images you will see one pizel is black and next is white


