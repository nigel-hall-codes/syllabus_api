import numpy as np
import cv2
import image
import pytesseract

class Syllabus:

    def __init__(self, img):
        self.cleaned_image = None
        self.image = image


    def clean_image(self):
        mask1 = np.zeros(self.image.shape, np.uint8)

        # convert image to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Create rectangular structuring element and use it for dilation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        dilate = cv2.dilate(thresh, kernel, iterations=4)

        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        x, y, w, h = cv2.boundingRect(contours)
        # create a mask to match location of text box
        for i in range(x, (x + w)):
            for j in range(y, y + h):
                mask1[j][i] = 255
        # combine date and assignment text box into one rectangle
        cv2.rectangle(self.image, (x, y), (x + w, y + h), (36, 255, 12), 2)
        # only focus on what is inside rectangle (see image)
        self.cleaned_image = cv2.bitwise_and(self.image, mask1)

    def text(self):
        return pytesseract.image_to_string(self.cleaned_image)
