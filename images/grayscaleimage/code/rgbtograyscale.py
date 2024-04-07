import cv2
 
messi_image = cv2.imread("../images/messi.jpg",cv2.IMREAD_ANYCOLOR)

if messi_image is not None:
    grayscale_messi = cv2.cvtColor(messi_image,cv2.COLOR_BGR2GRAY)
    print("Sucessfully converted rgb to gray")

    cv2.imwrite('../images/grayscalemessi.jpg',grayscale_messi)
    grayscale_image_path = '../images/grayscalemessi.jpg'
else:
    print("The image could not be loaded. Check the file path.")
    grayscale_image_path = None

grayscale_image_path