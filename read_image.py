from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pprint import pprint

image = Image.open("D:\\Pycharm_Projects\\meta_data.jpg")
print(image)
info = image.getexif()
print("________________", info)
d = {}
for tag, value in info.items():
    key = TAGS.get(tag, tag)
    if key not in d:
        d[key] = str(value)


pprint(d)
