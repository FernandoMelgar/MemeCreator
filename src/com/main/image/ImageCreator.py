from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class ImageCreator:
    resources_url = "../../../resources/"
    imgs_url = resources_url + "img/"
    outs_url = resources_url + "img_out/"

    def __init__(self, font_family, color_config):
        self.font = ImageFont.truetype(ImageCreator.resources_url + "fonts/" + font_family + ".ttf", 24)
        self.img_width = 0
        self.img_height = 0
        if color_config == "light":
            self.font_color = "black"
            self.bg_color = "white"
        if color_config == "dark":
            self.font_color = "white"
            self.bg_color = "black"

    def create_meme(self, upper_text, lower_text, img_name, out_name):
        img = Image.open(ImageCreator.imgs_url + img_name).convert("RGB")
        self.img_width, self.img_height = img.size
        txt_img = self._create_upper_text(upper_text)
        out = self._merge_images(txt_img, img)
        out.save(ImageCreator.outs_url + out_name, "JPEG")

    def _create_upper_text(self, upper_text):
        formatted_text = self._format_text(upper_text)
        paragraphs_to_add = 1
        if formatted_text.count("\n") > 1:
            paragraphs_to_add = formatted_text.count("\n")
        text_img = Image.new('RGB', (self.img_width, 100 * paragraphs_to_add), self.bg_color)
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text((20, 20), formatted_text, self.font_color, font=self.font)
        return text_img

    def _format_text(self, upper_text):
        new_text = ""
        font_size = self.font.size
        width_font_size = font_size * .6
        current_size = 0
        for word in upper_text.split(" "):
            if word == "\n":
                current_size = 0
            if current_size + width_font_size * len(word) >= self.img_width - 40:
                new_text += "\n "
                current_size = 0
            new_text += word + " "
            current_size += width_font_size * len(word)
        return new_text

    def _merge_images(self, content_img, meme_img):
        content_width, content_height = content_img.size
        output_img = Image.new('RGB', (self.img_width, content_height + self.img_height), self.bg_color)
        output_img.paste(content_img, (0, 0))
        output_img.paste(meme_img, (0, content_height))
        return output_img
