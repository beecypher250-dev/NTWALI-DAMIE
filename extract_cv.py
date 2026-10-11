import os
from PyPDF2 import PdfReader

pdf_path = r'c:\Users\nicki\OneDrive\Desktop\nicki_portifolio\damie cv.pdf'
print('exists:', os.path.exists(pdf_path))
reader = PdfReader(pdf_path)
text = '\n'.join(page.extract_text() or '' for page in reader.pages)
print(text[:30000])
