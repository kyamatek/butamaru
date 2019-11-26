# 画像の読み込み
from PIL import Image

def importimg(path):
    img = Image.open(path)
    return img
