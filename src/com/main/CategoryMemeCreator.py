import os
from com.main.image.ImageCreator import ImageCreator
from com.main.image.TextMemesRepository import TextMemesRepository


class CategoryMemeCreator:
    categories = {"reclamo", "crying", "deseo"}

    def createByCategory(self, category):
        img_names = os.listdir(ImageCreator.imgs_url + "/" + category)
        image_creator = ImageCreator("OpenSans-SemiBold", "light")
        for img in img_names:
            for txt_meme in TextMemesRepository.text_memes[category]:
                img_name = category + "/" + img
                out_name = self._format_out_name(category, img, txt_meme)
                image_creator.create_meme(txt_meme.text, "", img_name, out_name)

    def create_by_season(self, number):
        for category in CategoryMemeCreator.categories:
            img_names = os.listdir(ImageCreator.imgs_url + "/" + category)
            image_creator = ImageCreator("OpenSans-SemiBold", "dark")
            for img in img_names:
                if int(img[:2]) == number:
                    for txt_meme in TextMemesRepository.text_memes[category]:
                        img_name = category + "/" + img
                        out_name = self._format_out_name(category, img, txt_meme)
                        image_creator.create_meme(txt_meme.text, "", img_name, out_name)

    def _format_out_name(self, category, img, txt_meme):
        return category + "/" + img.split(".")[0] + "__" + txt_meme.title + "." + img.split(".")[1]


if __name__ == '__main__':
    categoryCreator = CategoryMemeCreator()
    categoryCreator.create_by_season(1)
