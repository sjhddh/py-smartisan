from docx import Document
from docx.shared import Pt

document = Document('demo.docx')

style = document.styles['Normal']
font = style.font
font.bold = True

for paragraph in document.paragraphs:
    paragraph.style = document.styles['Normal']

document.save('demo.docx')


