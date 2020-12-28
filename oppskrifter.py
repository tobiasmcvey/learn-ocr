"""
Bruk openCV og tesseract til å scanne oppskrifter og lagre de som filer.
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
image_ocr("recipes/01.png", "recipe-files/del1")
image_ocr("recipes/02.png", "recipe-files/del2")
image_ocr("recipes/03.png", "recipe-files/del3")
image_ocr("recipes/04.png", "recipe-files/del4")
image_ocr("recipes/05.png", "recipe-files/del5")
image_ocr("recipes/06.png", "recipe-files/del6")
image_ocr("recipes/07.png", "recipe-files/del7")
image_ocr("recipes/08.png", "recipe-files/del8")
# %%
# Funksjon for å laste inn bilder og lagre de som søkbare PDFer
def image_pdf_ocr(image_path, output_pdf_file_name):
  image_text = pytesseract.image_to_pdf_or_hocr(image_path, lang='nor', config='--psm 1', extension='pdf')
  with open(output_pdf_file_name, 'wb') as f:
    f.write(image_text)
# %%
image_pdf_ocr("recipes/01.png", "recipe-files/del1.pdf")
image_pdf_ocr("recipes/02.png", "recipe-files/del2.pdf")
image_pdf_ocr("recipes/03.png", "recipe-files/del3.pdf")
image_pdf_ocr("recipes/04.png", "recipe-files/del4.pdf")
image_pdf_ocr("recipes/05.png", "recipe-files/del5.pdf")
image_pdf_ocr("recipes/06.png", "recipe-files/del6.pdf")
image_pdf_ocr("recipes/07.png", "recipe-files/del7.pdf")
image_pdf_ocr("recipes/08.png", "recipe-files/del8.pdf")