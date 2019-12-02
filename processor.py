# coding: utf-8
from PIL import Image

def make_new_img(img, func):
    #RGBに変換
    rgb_img = img.convert('RGB')
    #画像のサイズ取得
    width, height = rgb_img.size
    #同じサイズのRGB画像の定義
    new_img = Image.new('RGB',(width,height))

    for x in range(width):
        for y in range(height):
            func(rgb_img, new_img, x, y)

    return new_img

def rb_change(original_img, new_img, x, y):
    r,g,b = original_img.getpixel((x,y))
    #rとbを入れ替えてpixelをセット
    new_img.putpixel((x,y),(g,r,b,0))

#RGBのRを最大にする
def red_max(original_img, new_img, x, y):
    r,g,b = original_img.getpixel((x,y))
    #Rの値を最大にする
    r = 255
    #pixelのセット
    new_img.putpixel((x,y),(r,g,b,0))

