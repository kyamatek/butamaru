# coding: utf-8
# 画像の読み込み
from PIL import Image

def importing(path):
    img = Image.open(path)
    return img
