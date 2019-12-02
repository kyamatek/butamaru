# coding: utf-8
import importer
import processor
import exporter
import sys
import argparse

parser = argparse.ArgumentParser(description = '')

parser.add_argument('-f', default = './pig.png') #ファイルパス
parser.add_argument('-m', default = 0) #モード

args = parser.parse_args()

img = importer.importing(args.f)
new_img = processor.red_max(img)
exporter.exporting(new_img,'./output/output.png')
