from PIL import Image

# 画像の読み込み
def Import(path):
    img = Image.open(path)
    return img
