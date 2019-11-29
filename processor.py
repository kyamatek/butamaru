from PIL import Image

#RGBのRを最大にする
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

    return new_img