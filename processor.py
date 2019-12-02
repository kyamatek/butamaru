# coding: utf-8
from PIL import Image

#RGBのRを最大にする
def select(img,number):
    num=int(number)%2
    if num==0:#引数が偶数のとき
        return red_max(img)
    else:
        return rb_change(img)

def red_max(img):
    rgb_img = img.convert('RGB')
    width, height = rgb_img.size
    new_img = Image.new('RGB',(width,height))

    for x in range(height):
        for y in range(width):
            #ピクセルを取得
            r,g,b = rgb_img.getpixel((x,y))

            #Rの値を最大にする
            r = 255

            #pixelのセット
            new_img.putpixel((x,y),(r,g,b,0))
    print("Rが〜でっかくなっちゃった！")
    return new_img

def rb_change(img):
    #RGBに変換
    rgb_img = img.convert('RGB')
    #画像のサイズ取得
    width, height = rgb_img.size
    #同じサイズのRGB画像の定義
    new_img = Image.new('RGB',(width,height))

    for x in range(height):
        for y in range(width):
            #ピクセルを取得
            r,g,b = rgb_img.getpixel((x,y))
            #rとbを入れ替えてpixelをセット
            new_img.putpixel((x,y),(g,r,b,0))
    print("RとB「俺たち、、入れ替わってる？！」")
    return new_img
