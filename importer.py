# 画像の読み込み
from PIL import Image

def Import(path):
    img = Image.open(path)
    return img
