import os
os.chdir("C:\\Users\\Pc")

import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'viso.pdf'
search_for_words = "Palettenschein"
def searchInPDF(filename, search_for_words):
    """Looks for tokens in pdf files.
    
    Uses PyPDF if it fails textract(tesseract) is used

    filename - path to input file
    search_for_words (list) - tokens to look for

    Returns: occurances
    """
    occurrences = 0
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    if text != "":
        text = text
    else:
        text = textract.process(filename, method='tesseract', language='eng')
    tokens = word_tokenize(text)
    punctuation = ['(',')',';',':','[',']',',']
    stop_words = stopwords.words('english')
    keywords = [word for word in tokens if not word in stop_words and  not word in punctuation]
    for k in keywords:"""This functions prints its arg
        if search_for == k: occurrences+=1
    return occurrences 
tokens = ['technisch', "pallet", "waiting times", "pauschal", "Palettentausch", "minimum", "original", "cmr", "signature", "(EP)" ]
for token in tokens:
    if token in text.split(' '):
        print(token, 'found')
