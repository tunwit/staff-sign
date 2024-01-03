from PIL import Image ,ImageDraw ,ImageFont
import json
from fpdf import FPDF
import os
import math

pdf = FPDF()
with open("name.json", "r" ,encoding="utf8") as f:
                database = json.load(f)
fontig = ImageFont.truetype("FC Minimal Bold.ttf", 90)

for class_ in list(database.keys()):
    for person in database[class_]:
        fontname = ImageFont.truetype("MN MINIMON Bold.ttf", 300)
        img = Image.open("staffwithoutname.png")
        draw = ImageDraw.Draw(img)
        left = 510 - (fontname.getsize(f"P'{person[0]}")[0]/2)
        right = 510 + (fontname.getsize(f"P'{person[0]}")[0]/2)
        if left < 60 or right > 960:
          i = 450
          while left < 60 or right > 960:
              fontname = ImageFont.truetype("MN MINIMON Bold.ttf", i)
              i-=1
              left = 510 - (fontname.getsize(f"P'{person[0]}")[0]/2)
              right = 510 + (fontname.getsize(f"P'{person[0]}")[0]/2)

        draw.text((525, 1005),f"P'{person[0]}",(84,118,149),font=fontname,anchor='ms')
        draw.text((510, 990),f"P'{person[0]}",(255,255,255),font=fontname,anchor='ms')
        if len(person) == 3:
            draw.text((510, 1140),f"FB : {person[1]}",(255,255,255),font=fontig,anchor='ms')
        else:
            draw.text((510, 1140),f"IG : {person[1]}",(255,255,255),font=fontig,anchor='ms')
        draw.text((519, 1376),class_,(84,118,149),font=fontig,anchor='ms')
        draw.text((510, 1370),class_,(255,255,255),font=fontig,anchor='ms')
        img.save(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{person[0]}{class_.replace('/','')}.png")
print("Writing image Done")
print("Combining to pdf...")
files = os.listdir('./image')
for i in range(math.ceil(len(files)/3)):
    print(i)
    pdf.add_page(orientation='landscape')
    if i == 0:
        a,b,c = files[0:3]
        pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{a}",5,5,90,130)
        pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{b}",100,5,90,130)
        pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{c}",195,5,90,130)
    else:
        if len(files[i*3:(i+1)*3]) == 1:
            a = files[i*3:(i+1)*3][0]
            pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{a}",5,5,90,130)
        if len(files[i*3:(i+1)*3]) == 2:
            a,b = files[i*3:(i+1)*3]
            pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{a}",5,5,90,130)
            pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{b}",100,5,90,130)
        if len(files[i*3:(i+1)*3]) == 3:
            a,b,c = files[i*3:(i+1)*3]
            pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{a}",5,5,90,130)
            pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{b}",100,5,90,130)
            pdf.image(f"C:\\Users\\Tunwi\\Desktop\\Python project\\Stuff sign\\image\\{c}",195,5,90,130)

pdf.output("Staff sign.pdf", "F")

print("Process Complete")