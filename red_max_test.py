import processor
from PIL import Image
img = Image.open('pig.png')
new_img = processor.red_max(img)
new_img.show()