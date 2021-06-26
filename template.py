#Author: Pranav Sastry
#DateTime: 2021-06-25 20:07:39.015825 IST

from PIL import Image, ImageColor, ImageDraw, ImageFont
from PIL.ImageDraw import Draw


class Template:
    def __init__(self, height, width, background_color=(255,255,255,0), mode='RGBA'):
        self.image = Image.new(mode=mode, size=(height,width), color=background_color)

    def add_text(self, text, text_x, text_y, font_path, font_size, text_color):
        text_image = Image.new("RGBA", self.image.size, (255,255,255,0))
        font_path = f"./fonts/{font_path}"
        font = ImageFont.truetype(font=font_path, size=font_size)
        draw = ImageDraw.Draw(text_image)
        draw.text((text_x,text_y), text, font=font, fill=text_color)
        text_image = text_image.resize(size=self.image.size, resample=Image.LANCZOS)
        self.image = Image.alpha_composite(self.image, text_image)

    # TODO: Add a new_layer boolean

    def add_rectangle(self, location, fill=None, outline=None, width=1):
        rect_image = Image.new("RGBA", self.image.size, (255,255,255,0))
        draw = ImageDraw.Draw(rect_image)
        draw.rectangle(location, fill, outline, width)
        rect_image = rect_image.resize(size=self.image.size, resample=Image.LANCZOS)
        self.image = Image.alpha_composite(self.image, rect_image)

    def add_arc(self, location, start_angle, end_angle, fill=None, width=0):
        arc_image = Image.new("RGBA", self.image.size, (255,255,255,0))
        draw = ImageDraw.Draw(arc_image)
        draw.arc(location, start_angle, end_angle, fill, width)
        arc_image = arc_image.resize(size=self.image.size, resample=Image.LANCZOS)
        self.image = Image.alpha_composite(self.image, arc_image)

    def add_image(self, img_path, img_x, img_y, new_size=None):
        img = Image.open(img_path)
        if(new_size):
            img = img.resize(size=new_size, resample=Image.LANCZOS)
        img = img.resize(size=img.size, resample=Image.LANCZOS)
        self.image.paste(img, (img_x,img_y), img)

    def show_image(self):
        self.image = self.image.resize(self.image.size,resample=Image.LANCZOS)
        self.image.show()

    def save_image(self, path, quality=95):
        self.image.save(fp=path, quality=quality)

if __name__=='__main__':
    temp = Template(500,500)
    temp.add_text("World",400,100,'eastman/eastman-trial.extrabold.otf',30,(0,0,0,255))
    temp.add_image("/Users/pranavsastry/Downloads/dp_img.png", 200, 100, (50,50))
    # temp.add_rectangle(location=[(0,400),(500,500)],fill=(0,0,0,255),outline=(255,255,255,255),width=5)
    temp.add_arc(location=[(0,0),(500,500)],start_angle=0,end_angle=360,fill=(0,0,0,255),width=10)
    temp.show_image()
    # temp.save_image("/Users/pranavsastry/Downloads/test_pil.png",100)
