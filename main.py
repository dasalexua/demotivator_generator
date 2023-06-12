import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def error(text:str="An unknown error has occurred!"):
	print(text)
	input("Press any key to exit . . . ")
	sys.exit()

def loadFont(size, name="arial.ttf"):
	try:
		return ImageFont.truetype(f'data/{name}', size=size)
	except: error(f"Unable to get font: data/{name}")


# Main functions
def Generate(image:str,title:str=None,subtitle:str=None):
	#Create basic image
	img = Image.new("RGBA", (768, 490), "black")
	idraw = ImageDraw.Draw(img)
	idraw.rectangle([(79,29), (688,382)], width=3)

	#Open image
	try:
		imgd = Image.open(f"img/{image}").convert('RGBA').resize((600,346))
		img.paste(imgd, (84,32), imgd)
	except:
		error(f"Unable to open image: img/{image}")

	#Title
	if title != None:
		y = 400
		for line in textwrap.wrap(title[:100], width=50):
			w = idraw.textlength(line, loadFont(28, 'demotivator.ttf'))
			x = int((img.width - w) / 2)
			idraw.text((x, y), line, font=loadFont(28, 'demotivator.ttf'), fill="white")
			y += loadFont(28, 'demotivator.ttf').getlength(line)
	
	#Subtitle
	if subtitle != None:
		y = 450
		for line in textwrap.wrap(subtitle[:80], width=80):
			w = idraw.textlength(line, loadFont(16))
			x = int((img.width - w) / 2)
			idraw.text((x, y), line, font=loadFont(16), fill="white")
			y += loadFont(16).getlength(line)

	#Check image name
	if not os.path.exists(f"img/{image}"):
		name = f"img/{image}"
		img.save(name)
	else:
		num = 2
		name = f"img/{image[:-4]} ({num}).png"
		for _ in range(500):
			if os.path.exists(name): num += 1
			else: break
		img.save(name)
	error(f"Generated image successfully saved as: {name}")


#Questions
while True:
	a = input("Image name (in folder \"img/\"): ")
	if len(a) < 1: a = "img.png"

	b = input("Title: ")
	if len(b) < 1: b = None

	c = input("Subtitle: ")
	if len(c) < 1: c = None

	Generate(a, b, c)
	print('\n\n\n')