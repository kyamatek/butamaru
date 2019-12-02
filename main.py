# coding: utf-8
import importer
import processor
import exporter
import sys

args = sys.argv
function_select=args[1]#偶数ならR最大 奇数ならRB反転

img=importer.importing("./pig.png")
new_img=processor.select(img,function_select)
exporter.exporting(new_img,'./output/testpig.png')
