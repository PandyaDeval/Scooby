import pytesseract
import PIL
from PIL import Image
import cv2
import csv

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = 'ss.png'
imge = Image.open(img)
data=pytesseract.image_to_boxes(imge)

print(data)