import pyttsx3
import PyPDF2
book = open('ebook.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
speaker.say('Reading starting')
for num in range(20, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    speaker.say('Page end. Starting new page')
