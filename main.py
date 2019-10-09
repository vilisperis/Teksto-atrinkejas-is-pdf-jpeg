import os
os.chdir("C:\\Users\\Pc")

import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'viso.pdf'
search_for = "Palettenschein"
def searchInPDF(filename, key):
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
    for k in keywords:
        if key == k: occurrences+=1
    return occurrences 

print(searchInPDF(filename, search_for))