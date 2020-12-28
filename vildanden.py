"""
Bruk openCV og tesseract til å scanne bilder av Vildanden og lagre som tekstfil.
For å installere støtte for norsk på ubuntu
sudo apt-get install tesseract-ocr-nor
"""
# %%
import cv2
import pytesseract
# %%
# Sjekk at du har støtte for norsk i tillegg til andre språk
print(pytesseract.get_languages(config=''))
# Bør printe ut ['eng', 'nor', 'osd']
# %%
# Funksjon for å laste inn bilder og lagre de som filer
def image_ocr(image_path, output_txt_file_name):
  image_text = pytesseract.image_to_string(image_path, lang='nor', config='--psm 1')
  with open(output_txt_file_name, 'w+', encoding='utf-8') as f:
    f.write(image_text)
# %%
# Last inn bilder og konverter de til tekstfiler
image_ocr("images/vildanden.png", "images/vildanden.txt")
# %%
# Funksjon for å laste inn bilder og lagre de som søkbare PDFer
def image_pdf_ocr(image_path, output_pdf_file_name):
  image_text = pytesseract.image_to_pdf_or_hocr(image_path, lang='nor', config='--psm 1', extension='pdf')
  with open(output_pdf_file_name, 'wb') as f:
    f.write(image_text)
# %%
image_pdf_ocr("images/vildanden.png", "images/vildanden.pdf")