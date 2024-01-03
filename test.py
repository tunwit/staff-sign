import math
from PIL import Image ,ImageDraw ,ImageFont

fontname = ImageFont.truetype("MN MINIMON Bold.ttf", 100)
fontname2 = ImageFont.truetype("MN MINIMON Bold.ttf", 100)
img = Image.open("6a0338ed2bd77424.gif")
draw = ImageDraw.Draw(img)
draw.text((50, 50),f"WElcome",(255,255,255),font=fontname2,anchor='ms')
img.save("test.gif")