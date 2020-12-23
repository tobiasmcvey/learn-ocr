"""
Bruk openCV og tesseract til å scanne oppskrifter og lagre de som filer.
For å installere støtte for norsk:
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
image_ocr("recipes/01.jpg", "del1")
# %%
image_ocr("recipes/02.jpg", "del2")
# %%
image_ocr("recipes/03.jpg", "del3")
# %%
image_ocr("recipes/04.jpg", "del4")
# %%
image_ocr("recipes/05.jpg", "del5")
# %%
image_ocr("recipes/06.jpg", "del6")
# %%
image_ocr("recipes/07.jpg", "del7")
# %%
image_ocr("recipes/08.jpg", "del8")
# %%
