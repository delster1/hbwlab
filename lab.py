from pdf2image import convert_from_path
import pandas as pd
from PIL import Image
from pytesseract import pytesseract
pathToTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
imgPath = r"imgs\page16.jpg"

def convert():
    images = convert_from_path('test.pdf', 100)
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save('imgs\page'+ str(i) +'.jpg', 'JPEG')
# Store Pdf with convert_from_path function

img = Image.open(imgPath)
# convert()
pytesseract.tesseract_cmd = pathToTesseract
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
# print(text)
data = pytesseract.image_to_data(Image.open(imgPath) , output_type='data.frame')

words = data["text"]
confidences = data["conf"]
for i,o in enumerate(words):
    if confidences[i] <= 80 and confidences[i] != -1:
        print(o, " ",  confidences[i])
    # if o["text"] == "NaN":
    #     pass
    # else:
    #     print(o["conf"])
reprText = repr(text)