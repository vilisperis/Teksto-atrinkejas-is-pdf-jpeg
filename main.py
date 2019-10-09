import os
os.chdir("C:\\Users\\Pc")

international_words = "Palettenschein"
filename = 'viso.pdf' 
pdfFileObj = open(filename,'rb')
print(pdfFileObj)
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader)
num_pages = pdfReader.numPages
print(num_pages)
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()
    print(text)
if text != "":
    text = text
else:
   text = textract.process("fileurl", method='tesseract', language='eng')
print(text)

tokens = word_tokenize(text)
stop_words = stopwords.words('english')
keywords = [word for word in tokens if not word in stop_words and not word in string.punctuation]

for i in range(0, num_pages):
    pageObj = pdfReader.getPage(i)
    print("this is page " + str(i)) 
    text = pageObj.extractText() 
    print(text)
    ResSearch = re.search(international_words, text)
    print(ResSearch)