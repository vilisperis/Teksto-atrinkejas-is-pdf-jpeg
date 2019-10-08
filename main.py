input_path_file = "pdf"
international_words = ["kein tausch", "palettenshein", 'status', "cmr", "parking", "waiting time", "penalty", "tauschen", "safety"]
import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'uzsakymas'
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
   text = textract.process(fileurl, method='tesseract', language='eng')
print(text)
