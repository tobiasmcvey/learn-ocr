"""
Learn to use openCV and tesseract for opening and reading text from picture files
"""
# %%
import cv2
import pytesseract

# %%
img = cv2.imread("800px-Wikinews_Breaking_News.png")
text = pytesseract.image_to_string(img)
print(text)
# %%
img = cv2.imread("bitcoin.jpeg")
text = pytesseract.image_to_string(img)
print(text)
# %%
