import pytesseract	 
from PIL import Image	 
import pyttsx3		 
import googletrans
from googletrans import Translator	
import cv2 
import numpy as np
# print(googletrans.LANGUAGES)


def image_smoothening(img):
    ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (1, 1), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3

def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name, 0)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image


BINARY_THREHOLD = 180

# Image Read and Preprocessing:
img = cv2.imread('text1.png',0)
# img = remove_noise_and_smooth('text1.png')

# cv2.imshow(str(img),img)
# cv2.waitKey(0)
# cv2.imshow(str(img1),img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# path where the tesseract module is installed 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

# Extract text from image
result = pytesseract.image_to_string(img) 
with open('detected_text.txt',mode ='w') as file:	 
				file.write(result) 
				# print(result.encode('utf-8')) 
				
# Translate extracted text to destination language 
p = Translator()
k = p.translate(result,dest='english')	 # german , french
print(k.text)


# Text to speech 
engine = pyttsx3.init() 
engine.say(k.text)							 
engine.runAndWait() 
