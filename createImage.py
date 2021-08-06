from PIL import ImageDraw, ImageFont, Image
import textwrap


class CreateImage:


    def __init__(self, your_name=False, background='./image/reflex.jpg'):
        self.background = background
        self.yourName = your_name


    def create(self, text, name='teste', size=60):
        himageText = 0
        im = Image.open(self.background)
        width, height = im.size # size of image
        drow = ImageDraw.Draw(im)

        l_text = (round(width / size) * 2) - 10

        text = textwrap.wrap(text, width=l_text) #30
        
        neutro = round((width - (len(text) * size)) / 2)
        for c in text:

            font = ImageFont.truetype('arial.ttf', 60) # create font image
            wText, hText = font.getsize(c)

            drow.text(xy=((width - wText) / 2, neutro), text=c, font=font)
            neutro += 60


        if (self.yourName):
            font_name = ImageFont.truetype('arial.ttf', size=30)
            w, h = font.getsize(self.yourName)
            drow.text(xy=(width - (w + 10), height - (h + 10)), text=f'{self.yourName}', font=font_name, stroke_width=5,fill='white', stroke_fill='black')
        
        im.save(f'./image/new/{name}.jpg')


