import pprint as pr
from pdf2image import convert_from_path
import pandas as pd
from PIL import Image
from pytesseract import pytesseract
pathToTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def convertPdfToJpg(pdfPath): # duh
    images = convert_from_path('test.pdf', 100) # adds pages from pdf to folder of imgs
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save('imgs\page'+ str(i) +'.jpg', 'JPEG')
        # Store Pdf with convert_from_path functionpy


def convertPageToData(imgPath): # duh
    img = Image.open(imgPath)
    pytesseract.tesseract_cmd = pathToTesseract
    
    out = pytesseract.image_to_data(Image.open(imgPath) , output_type='data.frame')


    return out

def findBadConfidences(data,confidencePercent):
    out = {}
    words = data["text"] # array of words
    confidences = data["conf"] # array of confidences
    for wordIndex, word in enumerate(words):
        if confidences[wordIndex] <= confidencePercent and confidences[wordIndex] != -1 and confidences[wordIndex] != 0: # find confidences below a confidencePercent
            wordConfidence = confidences[wordIndex]

            out[word] = wordConfidence # add to dict
            

        
    return out

def find(s, el):
    for i in s.index:
        if s[i] == el: 
            return i
    return None

def getBadWordData(badWordsToSearch, data, toFind):
    out = "not changed"

    if type(badWordsToSearch) == dict: 

        for badWord in badWordsToSearch:
            if badWord == toFind:
                print("\nfound:", toFind,"\n")

                outIndex = find(data["text"],toFind)
                out = data.loc[outIndex]
                break
    print("output: ", out,"\n")
    
    return out

def pageToRepr(pagePath):


    text = pytesseract.image_to_string(pagePath) # convert path to text
    reprText = repr(text) # duh

    return text, reprText

def main():
    

    pdf = "test.pdf" #pdf to use
    pagePath = r"imgs\page35.jpg" #page to parse

    bestConfidence = 75
    # convertPdfTo(pdf)

    data = convertPageToData(pagePath) #turn page into data of confidences for words etc
    # pr.pprint(data)

    badConfidencesDict = findBadConfidences(data, bestConfidence)
    print(badConfidencesDict)
    getBadWordData(badConfidencesDict, data, list(badConfidencesDict)[1])

    pgText = pageToRepr(pagePath)

    arrayBySentences = pgText[0].split(".")

    for sentence in arrayBySentences:
        toSearch = list(badConfidencesDict)[1]
        if toSearch in sentence:
            print(sentence)
    


if __name__ == "__main__":
    main()