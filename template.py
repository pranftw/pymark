#Author: Pranav Sastry
#DateTime: 2021-06-25 20:07:39.015825 IST

from PIL import Image, ImageColor, ImageDraw, ImageFont
from PIL.ImageDraw import Draw


class Template:
    def __init__(self, height, width, background_color='#ffffff', mode='RGBA'):
        self.image = Image.new(mode=mode, size=(height,width), color=ImageColor.getrgb(background_color))

    def add_text(self, text, text_x, text_y, font_path, font_size, text_color):
        text_image = Image.new("RGBA", self.image.size, (255,255,255,0))
        font_path = f"./fonts/{font_path}"
        font = ImageFont.truetype(font=font_path, size=font_size)
        draw = ImageDraw.Draw(text_image)
        draw.text((text_x,text_y), text, font=font, fill=text_color)
        self.image = Image.alpha_composite(self.image, text_image)

    def add_graphics(self):
        pass

    def add_image(self, img_path):
        pass

    def show_image(self):
        self.image.show()

if __name__=='__main__':
    temp = Template(500,500)
    temp.add_text("World",400,100,'eastman/eastman-trial.extrabold.otf',30,(0,0,0,255))
    temp.show_image()
