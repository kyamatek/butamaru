# coding: utf-8
import importer
import processor
import exporter

img=importer.importing("./pig.png")
new_img=processor.rb_change(img)
exporter.exporting(new_img,'./output/testpig.png')
