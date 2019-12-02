import exporter
from PIL import Image
img = Image.open('./input/pig.png')
exporter.exporting(img, './output/test_pig.png')