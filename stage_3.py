from PIL import Image, ImageDraw, ImageFont

# Open the image
image = Image.open("test.jpg")

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Define the font and size
font = ImageFont.truetype("Roboto-Bold.ttf", 36)

# Define the text and position
text = "Hello, World!"
text_x, text_y = (50, 50)

# Draw the text on the image
draw.text((text_x, text_y), text, font=font, fill=(255, 0, 0))

# Save the image
image.save("image_with_text.jpg")
