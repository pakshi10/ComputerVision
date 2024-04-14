import cv2

def scale_image(image_path, output_dim, keep_aspect_ratio=True):
    # Read the image from the specified path
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"The image at {image_path} could not be loaded.")
    
    # Obtain the original dimensions
    original_height, original_width = image.shape[:2]

    if keep_aspect_ratio:
        # Calculate the ratio and determine new dimensions
        ratio = min(output_dim[0] / original_width, output_dim[1] / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
    else:
        new_width, new_height = output_dim
    
    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    return resized_image

# Example usage
if __name__ == "__main__":
    # Path to the input image
    image_path = '../image/messi.jpg'
    # Desired output dimensions (width, height)
    output_dimensions = (224, 224)  # Common size for CNNs like VGG or ResNet
    
    # Scale the image
    scaled_image = scale_image(image_path, output_dimensions, keep_aspect_ratio=False)
    
    # Save or display the scaled image
    cv2.imshow('Scaled Image', scaled_image)
    cv2.waitKey(0)  # Wait for a key press to close the image window
    cv2.destroyAllWindows()

'''
Explanation of the Code

    Importing OpenCV: The script starts by importing the necessary OpenCV library.
    Function Definition: The function scale_image takes the path to an image, the desired output dimensions, and a flag to keep the aspect ratio.
    Reading the Image: The image is loaded from the specified path.
    Aspect Ratio Management: If the aspect ratio is to be preserved, the function calculates the new dimensions based on the smaller ratio of width or height scaling factor.
    Resizing the Image: OpenCV's resize method is used to scale the image. The INTER_AREA interpolation is efficient for shrinking.
    Usage Example: The main block tests the function using a specified path and dimensions, showing the resulting image using OpenCV's display functions.

'''