#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:42:21 2022

@author: waqas
"""
import os
import shutil

directory = '/Users/waqas/Desktop/keras-yolo3-master/data/JPEGImages'
ext1 = ".jpg"
ext2 = ".png"
ext3 = ".jpeg"

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        print(os.path.join(directory, filename))
        filename1 = filename + ext1
        filename2 = filename + ext2
        filename3 = filename + ext3
        
        src_path = os.path.join(directory, filename)
        
        tp1 = os.path.join(directory, filename1)
        tp2 = os.path.join(directory, filename2)
        tp3 = os.path.join(directory, filename3)
        
        shutil.copyfile(src_path,tp1)
        print(tp1)
        shutil.copyfile(src_path,tp2)
        print(tp2)
        shutil.copyfile(src_path,tp3)
        print(tp3)
    else:
        print("File did not match extension")
        continue