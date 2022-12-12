#imports 
import pprint as pr
from pdf2image import convert_from_path
from PIL import Image, ImageDraw
from spellchecker import SpellChecker
spell = SpellChecker()

#tesseract setup
from pytesseract import pytesseract
pathToTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = pathToTesseract
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'


def convertPdfToJpg(pdfPath): # duh
    images = convert_from_path('test.pdf', 100) # adds pages from pdf to folder of imgs
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save('imgs\page'+ str(i) +'.jpg', 'JPEG')
        # Store Pdf with convert_from_path functionpy

def convertPageToDataframe(imgPath):
    img = Image.open(imgPath)
    pytesseract.tesseract_cmd = pathToTesseract
    
    out = pytesseract.image_to_data(Image.open(imgPath) , output_type='data.frame',config=tessdata_dir_config)


    return out

def convertPageToData(imgPath): # duh
    img = Image.open(imgPath)
    pytesseract.tesseract_cmd = pathToTesseract
    
    out = pytesseract.image_to_data(Image.open(imgPath) , output_type='dict',config=tessdata_dir_config)


    return out

def findBadConfidencesAndLocations(data,confidencePercent):
    out = {}

    for i in range(len(data["text"])):
  # check if the confidence is low
        if int(data["conf"][i]) < confidencePercent:
            # output the word and its location
            out[data["text"][i]] = data["left"][i], data["top"][i]
        
    return out

def find(s, el):
    for i in s.index:
        if s[i] == el: 
            return i
    return None

def getBadWordData(badWordsToSearch, data, toFind): 
    out = "not changed"

    return out

def pageToRepr(pagePath):
    pytesseract.tesseract_cmd = pathToTesseract


    text = pytesseract.image_to_string(pagePath,config=tessdata_dir_config) # convert path to text
    reprText = repr(text) # duh

    return text, reprText

def makeArrayOfLines(reprText):
    out = reprText.split("\n")
    return out

def writeToFile(toWriteToFile, file):
    with open("pgScan.txt","w",encoding="utf8") as f:
        f.writelines(toWriteToFile)

def drawWordLocations(badConfidencesDict, pgImage):
    draw = ImageDraw.Draw(pgImage)

    for o in badConfidencesDict.values():
        
        x=o[0]
        y=o[1]
        draw.ellipse((x-10, y-10, x+10, y+10), fill=(0, 255, 0, 100))
    #     f.writelines(pgText[0])
    pgImage.show()

def main():
        #TODO ADD CORRECT WORD DETECTION (detecting words that are already spelled correctly and probably do not need to be corrected)

    
    pdf = "test.pdf" #pdf to use
    pagePath = r"imgs\page56.jpg" #page to parse
    pgImage = Image.open(pagePath)
    confidencePercent = 80
    # convertPdfTo(pdf)
    print("confidence theshold: ", confidencePercent, "%\n")
    data = convertPageToData(pagePath) #turn page into data of confidences for words etc
    # pr.pprint(data)
    
    badConfidencesDict = findBadConfidencesAndLocations(data, confidencePercent)
    pr.pprint(badConfidencesDict)
    print("\nNumber of low confidence words: " + str(len(badConfidencesDict)))
    # getBadWordData(badConfidencesDict, data, list(badConfidencesDict)[1])

    pgText = pageToRepr(pagePath)

    arrayBySentences = pgText[0].split(".")
    arrayOfLines = makeArrayOfLines(pgText[1])

    print(convertPageToDataframe(pagePath))

    writeToFile(pgText[0], "pgScan.txt")
    
    drawWordLocations(badConfidencesDict, pgImage)
    


if __name__ == "__main__":
    main()