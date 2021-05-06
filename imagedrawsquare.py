from PIL import Image, ImageDraw
from time import sleep
import os
import guiSetup

def imgGen(values):
    #monitor size
    height=values[0]
    width=values[1]
    #background color
    bgR=values[2]
    bgG=values[3]
    bgB=values[4]
    #line color
    R=values[5]
    G=values[6]
    B=values[7]
    #line thickness
    lineWidth=values[8]
    #Filename
    fn=values[9]
    #instantiate image & draw
    img = Image.new('RGB', (width, height), (bgR, bgG, bgB))
    draw = ImageDraw.Draw(img)

    #x lines
    draw.line(((lineWidth/2), height, (lineWidth/2), 0), fill=(R, G, B), width=lineWidth)                                   #left
    draw.line((width-lineWidth+(lineWidth/2), height, width-lineWidth+(lineWidth/2), 0), fill=(R, G, B), width=lineWidth)   #right

    # top line offset
    offset=(lineWidth/2)-1 if (lineWidth % 2 == 0)  else (lineWidth/2)
    
    #y lines
    draw.line((0, offset, width, offset), fill=(R, G, B), width=lineWidth)                                     #top
    draw.line((0, height-lineWidth+(lineWidth/2), width, height-lineWidth+(lineWidth/2)),fill=(R, G, B), width=lineWidth)    #bottom

    #img.show()
    fn=fn+".png"
    print(fn)
    img.save(fn)
    return
