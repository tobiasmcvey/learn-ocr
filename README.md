# Notes from learning OCR

Examples using Tesseract and OpenCV to convert pictures to text. 

Installing tesseract adds support for English. To support additional languages, install it separately or [install all available languages](https://askubuntu.com/a/798492).

[introduction.py](introduction.py) is an introduction script to show how to parse text from an image with interactive python.

[oppskrifter.py](oppskrifter.py) is an example of converting pictures with recipes in Norwegian to text files and searchable PDF files. 

[vildanden.py](vildanden.py) is an example of converting a picture of the starting act of Vildanden by Henrik Ibsen, into a text file and a searchable PDF. See the image from [Vildanden on Project Gutenberg](https://www.gutenberg.org/ebooks/13041) provided under Public Domain in the USA.

# Setup

On linux

```
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

and install dependencies in requirements file with `pip install -r requirements.txt`

converted .jpg files to .png for easier conversion using [ffmpeg](https://ffmpeg.org/) using `ffmpeg -i input.jpg output.png`
