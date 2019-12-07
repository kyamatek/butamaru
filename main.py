# coding: utf-8
import importer
import processor
import exporter
import argparse

#コマンドライン引数の定義
parser = argparse.ArgumentParser(description = '')

parser.add_argument('-f', default = './input/pig.png') #ファイルパス
parser.add_argument('-m', default = 0) #モード

args = parser.parse_args()


img = importer.importing(args.f)
if args.m==0:
    new_img = processor.make_new_img(img, processor.red_max)
else:
    new_img = processor.make_new_img(img, processor.rb_change)
    
exporter.exporting(new_img,'./output/output.png')
