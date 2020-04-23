import pytesseract
from pytesseract import Output
from PIL import Image, ImageDraw, ImageFont
import sys
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\chotu\AppData\Local\Tesseract-OCR\tesseract.exe'
im = Image.open("RemoveTest.jpg") # the second one

def remove_text(im):
    text = pytesseract.image_to_data(im, output_type=Output.DICT)
    n_boxes = len(text['level'])
    word_set = set()
    corr = 3
    for i in range(n_boxes):
        (x, y, w, h) = (text['left'][i], text['top'][i], text['width'][i], text['height'][i])
        word_set.add((x - corr, y - corr, x + w + corr, y + h + corr))
    for w in word_set:
        i = im.crop(box = w)
        text = pytesseract.image_to_string(i).strip().lower()
        if (len(text) > 0 and text in ["no one:", "noone:", "nobody:", "no body:", "not a single soul:"]):
            ImageDraw.Draw(im).rectangle(w, fill=(255,255,255))
    return im


img = Image.new('RGB', (960, 720), color=(255,255,255))
fnt = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 30)
d = ImageDraw.Draw(img)
d.text((100, 100), "No body:", font = fnt, fill=(255,255,0))
