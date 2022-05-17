#! /usr/bin/env python3
from random import randint
from PIL import Image, ImageDraw, ImageFont
from itsdangerous import json


def add_color(image,c,transparency):
    color = Image.new('RGB',image.size,c)
    mask = Image.new('RGBA',image.size,(0,0,0,transparency))
    return Image.composite(image,color,mask).convert('RGB')

def center_text(img,font,text1,text2,fill1,fill2):
    draw = ImageDraw.Draw(img) # Initialize drawing on the image
    w,h = img.size # get width and height of image
    t1_width, t1_height = draw.textsize(text1, font) # Get text1 size
    t2_width, t2_height = draw.textsize(text2, font) # Get text2 size
    p1 = ((w-t1_width)/2,h // 3) # H-center align text1
    p2 = ((w-t2_width)/2,h // 3 + h // 5) # H-center align text2
    draw.text(p1, text1, fill=fill1, font=font) # draw text on top of image
    draw.text(p2, text2, fill=fill2, font=font) # draw text on top of image
    draw.text(p2, text2, fill=fill2, font=font) # draw text on top of image
    return img

def add_text(img,color,text1,text2,logo=False,font='Roboto-Bold.ttf',font_size=75):#change font_size
    draw = ImageDraw.Draw(img)
 
    s_font = color['p_font']
    p_font = color['s_font']
     
    # starting position of the message
    img_w, img_h = img.size
    height = img_h // 3
    font = ImageFont.truetype(font,size=font_size)
 
    if logo == False:
        center_text(img,font,text1,text2,p_font,s_font)
    else:
        subtract=50
        text1_offset = (img_w // 8, height-subtract)
        text2_offset = (img_w // 8, (height + img_h // 5)-subtract)
        draw.text(text1_offset, text1, fill=p_font, font=font)
        draw.text(text2_offset, text2, fill=s_font, font=font)
        draw.text((((img_w // 2)+300, (height + img_h // 2))), "@tauseedzaman", fill=(93,188,210), font=font)
    return img

def add_logo(background,foreground):
    bg_w, bg_h = background.size
    img_offset = (390, (bg_h //3))#390,160 #
    background.paste(foreground, img_offset, foreground)
    return background
def write_image(background,color,text1,text2,foreground=''):
    background = add_color(background,color['c'],99)
    if not foreground:
        add_text(background,color,text1,text2)
    else:
        add_text(background,color,text1,text2,logo=True)
    return background
    
if __name__ == '__main__':
    with open("commands.json") as command:
        commands=json.load(command)
    list=0
    tauseedzaman = '@tauseed2aman'
    bgcolors=['dark_blue','grey','light_blue','blue','orange','purple','red','yellow','yellow_green','green']
    color = 'dark_blue'
    font = 'Roboto-Bold.ttf'
    
    foreground = Image.open('src/logo.png')
    colors = {
    'dark_blue':{'c':(27,53,81),'p_font':'rgb(255,255,255)','s_font':'rgb(255, 212, 55)'},
    'grey':{'c':(70,86,95),'p_font':'rgb(255,255,255)','s_font':'rgb(93,188,210)'},
    'light_blue':{'c':(93,188,210),'p_font':'rgb(27,53,81)','s_font':'rgb(255,255,255)'},
    'blue':{'c':(23,114,237),'p_font':'rgb(255,255,255)','s_font':'rgb(255, 255, 255)'},
    'orange':{'c':(242,174,100),'p_font':'rgb(0,0,0)','s_font':'rgb(0,0,0)'},
    'purple':{'c':(114,88,136),'p_font':'rgb(255,255,255)','s_font':'rgb(255, 212, 55)'},
    'red':{'c':(255,0,0),'p_font':'rgb(0,0,0)','s_font':'rgb(0,0,0)'},
    'yellow':{'c':(255,255,0),'p_font':'rgb(0,0,0)','s_font':'rgb(27,53,81)'},
    'yellow_green':{'c':(232,240,165),'p_font':'rgb(0,0,0)','s_font':'rgb(0,0,0)'},
    'green':{'c':(65, 162, 77),'p_font':'rgb(217, 210, 192)','s_font':'rgb(0, 0, 0)'}
    }
    for i,command in enumerate(commands["data"]):
        bg_image_name=('src/background-'+str(randint(4,17))+'.jpg')
        background = Image.open(bg_image_name)
        l=len(command["description"])
        if i == 4:
            continue
        if i == 8:
            break
        if l >= 40:
            description=(command["description"].split())
            description.insert(5,"\n")
            description=" ".join(description)


        else:
            description=command["description"]
        background = write_image(background,colors[bgcolors[randint(0,9)]],"$ "+command["command"],description,foreground=foreground)
        background.save("out/"+command["command"]+".png")
        print(description)
