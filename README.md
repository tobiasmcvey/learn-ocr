# Notes from learning OCR

Examples using Tesseract and OpenCV to convert pictures to text. 

Installing tesseract adds support for English. To support additional languages, install it separately or [install all available languages](https://askubuntu.com/a/798492).

[introduction.py](introduction.py) is an introduction script to show how to parse text from an image with interactive python.

[oppskrifter.py](oppskrifter.py) is an example of converting pictures with recipes in Norwegian to text files and searchable PDF files. 

# Setup

On linux

```
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

and install dependencies in requirements file with `pip install -r requirements.txt`