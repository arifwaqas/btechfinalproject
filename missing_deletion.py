#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:37:45 2022

@author: waqas
"""

import random
from PIL import Image

s=open("/Users/waqas/Desktop/keras-yolo3-master/2007_traincopy.txt","r")
lines=s.readlines()
count = 0
for i in lines:
    line = i.split()
    #image = Image.open(line[0])
    try:
        image = Image.open(line[0])
    except:
        print(line[0])
        count = count+1
        continue
    
    #print("Open successful")
    
print("Total count of missing: " + str(count) + " out of " + str(len(lines)))
s.close()