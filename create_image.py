#! /usr/bin/env python3
import requests
from random import randint
from PIL import Image, ImageDraw, ImageFont
import json
import urllib.request

command=""

def add_color(image, c, transparency):
    color = Image.new('RGB', image.size, c)
    mask = Image.new('RGBA', image.size, (0, 0, 0, transparency))
    return Image.composite(image, color, mask).convert('RGB')


def center_text(img, font_1, font_2, text1, text2, fill1, fill2):
    draw = ImageDraw.Draw(img)  # Initialize drawing on the image
    w, h = img.size  # get width and height of image
    t1_width, t1_height = draw.textsize(text1, font_1)  # Get text1 size
    t2_width, t2_height = draw.textsize(text2, font_2)  # Get text2 size

    # Draw the shadow text on the image
    p1 = ((w-t1_width)/2, h // 3)  # H-center align text1
    p2 = ((w-t2_width)//2, h // 3 + h // 5)  # H-center align text2
    # p2 = ((w-t2_width)/2, h // 3 + h // 5)  # H-center align text2
    draw.text(p1, text1, fill=fill1, font=font_1)  # draw text on top of image
    draw.text(p2, text2, fill=fill2, font=font_2)  # draw text on top of image
    # draw.text(p2, text2, fill=fill2, font=font)  # draw text on top of image
    return img


def add_text(img, color, text1, text2, logo=False, font='Roboto-Bold.ttf', font_size=250):  # change font_size
    draw = ImageDraw.Draw(img)

    s_font = color['p_font']
    p_font = color['s_font']

    # starting position of the message
    img_w, img_h = img.size
    height = img_h // 3
    font_1 = ImageFont.truetype(font, size=font_size)
    font_2 = ImageFont.truetype(font, size=100)

    center_text(img, font_1, font_2, text1, text2, p_font, s_font)
    return img


def add_logo(background, foreground):
    bg_w, bg_h = background.size
    img_offset = (390, (bg_h // 3))  # 390,160 #
    background.paste(foreground, img_offset, foreground)
    return background


def write_image(background, color, text1, text2, foreground=''):
    background = add_color(background, color['c'], 99)
    # if not foreground:
    add_text(background, color, text1, text2)
    # else:
    # add_text(background, color, text1, text2)
    # print("s")
    return background


def get_command_name():
    file_path = "commands.txt"

    # Open the file in read mode
    with open(file_path, "r") as file:
        first_line = file.readline()

        # Get all the lines after the first one
        # lines = file.readlines()

    # # Open the file in write mode
    # with open(file_path, "w") as file:
    #     # Write all the lines except the first one to the file
    #     file.writelines(lines)
    return first_line


def create_message_by_open_api():

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }

    command_name = get_command_name()
    command=command_name

    data = {
        "model": "text-davinci-003",
        "prompt": f"tell me about {command_name} in kali Linux in one sentence and give me one example as well",
        "temperature": 0,
        "max_tokens": 200
    }

    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data))
    print(f"command: {command_name}")
    print(response.json()["choices"][0]["text"])
    return response.json()["choices"][0]["text"]


def get_random_image_from_unsflash():
    url = "https://api.unsplash.com/photos/random?query=cumputer&topics=Technology&count=1&orientation=landscape&client_id=net7NdcVyXVCFXaEn9obXSTUWGy6OXVX69zyFmfJ2gA"
    response = requests.get(url)
    img_url=response.json()[0]["urls"]["raw"]
    # return response.json()[0]["urls"]["raw"]

    # Define the local file name
    file_name = "image.jpg"

    # Download the image and save it to the local file
    urllib.request.urlretrieve(img_url, file_name)
    return file_name



if __name__ == '__main__':
    img =get_random_image_from_unsflash()
    #  "test.jpg"
    message = create_message_by_open_api()
    message=message.replace("example:","\n\n example:")
    tauseedzaman = '@realtauseed'
    bgcolors = ['dark_blue', 'grey', 'light_blue', 'blue',
                'orange', 'purple', 'red', 'yellow', 'yellow_green', 'green']
    color = 'dark_blue'
    font = 'Roboto-Bold.ttf'

    foreground = "xx"
    colors = {
        'dark_blue': {'c': (27, 53, 81), 'p_font': 'rgb(255,255,255)', 's_font': 'rgb(255, 212, 55)'},
        'grey': {'c': (70, 86, 95), 'p_font': 'rgb(255,255,255)', 's_font': 'rgb(93,188,210)'},
        'light_blue': {'c': (93, 188, 210), 'p_font': 'rgb(27,53,81)', 's_font': 'rgb(255,255,255)'},
        'blue': {'c': (23, 114, 237), 'p_font': 'rgb(255,255,255)', 's_font': 'rgb(255, 255, 255)'},
        'orange': {'c': (242, 174, 100), 'p_font': 'rgb(0,0,0)', 's_font': 'rgb(0,0,0)'},
        'purple': {'c': (114, 88, 136), 'p_font': 'rgb(255,255,255)', 's_font': 'rgb(255, 212, 55)'},
        # 'red': {'c': (255, 0, 0), 'p_font': 'rgb(0,0,0)', 's_font': 'rgb(0,0,0)'},
        'yellow': {'c': (255, 255, 0), 'p_font': 'rgb(0,0,0)', 's_font': 'rgb(27,53,81)'},
        'yellow_green': {'c': (232, 240, 165), 'p_font': 'rgb(0,0,0)', 's_font': 'rgb(0,0,0)'},
        'green': {'c': (65, 162, 77), 'p_font': 'rgb(217, 210, 192)', 's_font': 'rgb(0, 0, 0)'}
    }
    background = Image.open(img)
    background = write_image(background, colors[bgcolors[randint(
        0, 9)]], "$_ "+"command", message, foreground=foreground)
    background.save("xx.png")
    print(message)
