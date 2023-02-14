import os
import cv2
import shutil
from flask import *
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':

        # Get the list of files from webpage
        files = request.files.getlist("file")

        # Iterate for each file in the files List, and Save them
        for file in files:
            file.save(f"D:\\riyaproject\\uploads\\{file.filename}")
        all_text=read_fun("D:\\riyaproject\\uploads")
        for file in files:
            os.remove(f"D:\\riyaproject\\uploads\\{file.filename}")
        return render_template("show_text.html",variable=all_text)

def read_fun(path_uploads):
    list_imgs=os.listdir(path_uploads)
    list_imgs=[f"{path_uploads}\\{i}" for i in list_imgs]
    all_text=[]
    for img in list_imgs:
        image = cv2.imread(img)
        text=ocr(image)
        all_text.append(text)
    return all_text

def ocr(img):
    text=pytesseract.image_to_string(img)
    return text


if __name__ == '__main__':
    app.run(debug=True)