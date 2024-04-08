import cv2
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread('../images/messi.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Split the image into RGB channels
R, G, B = cv2.split(image)

# Display each channel and the original image
fig, axs = plt.subplots(1, 4, figsize=(20, 5))
axs[0].imshow(R, cmap='Reds')
axs[0].set_title('Red Channel')
axs[0].axis('off')

axs[1].imshow(G, cmap='Greens')
axs[1].set_title('Green Channel')
axs[1].axis('off')

axs[2].imshow(B, cmap='Blues')
axs[2].set_title('Blue Channel')
axs[2].axis('off')

axs[3].imshow(image)
axs[3].set_title('Original Image')
axs[3].axis('off')

plt.show()