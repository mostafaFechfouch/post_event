# -*- coding: utf-8 -*-

import unicodecsv as csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

#The horizontal and vertical coordinates to type the name
horizontal=1750
vertical=1100

with open(u'testing.csv','rb') as csvfile:
    reader = csv.reader(csvfile, encoding="utf-8") 
    for row in reader: 
        img = Image.open("certificate.png").convert("RGB")
        draw = ImageDraw.Draw(img)
        bidi_text=row[0]
        if row[1].isalnum():
            selectFont = ImageFont.truetype("PortamentoMono-Light.otf", size = 135)
        else:
            text_to_be_reshaped=row[1]
            reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
            bidi_text = get_display(reshaped_text)
            selectFont=ImageFont.truetype("arial.ttf", size = 135)
        w, h = draw.textsize(bidi_text, font=selectFont)
        draw.text( (horizontal-w/2,vertical), bidi_text , (33,33,32), font=selectFont)
        img.save( 'certifications/certificate_'+row[0].split("@")[0]+'.pdf', "PDF", resolution=100.0)

