import numpy as np
import cv2

# Define the size of the chessboard, each square, and the total image
board_size = 8
square_size = 50
image_size = board_size * square_size

# Create a black image
chessboard = np.zeros((image_size, image_size), dtype=np.uint8)

# Set white squares (255) on the chessboard
for i in range(board_size):
    for j in range(board_size):
        if (i + j) % 2 == 1:
            chessboard[i * square_size:(i + 1) * square_size,
                       j * square_size:(j + 1) * square_size] = 255

# Save the chessboard image
cv2.imwrite('../images/chessboard.png', chessboard)
