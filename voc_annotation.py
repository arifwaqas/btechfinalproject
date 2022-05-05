import xml.etree.ElementTree as ET
from os import getcwd
import os 

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["car", "plate"]


def convert_annotation(year, image_id, list_file):
    
    image_id2 = os.path.splitext(image_id)[0]
    
    try:
        in_file = open('/Users/waqas/Desktop/keras-yolo3-master/data/Annotations/%s.xml'%(image_id2))
    except:
        print('%s.xml'%(image_id2))
        return
    
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)), int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('/Users/waqas/Desktop/keras-yolo3-master/data/ImageSets/Main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('/Users/waqas/Desktop/keras-yolo3-master/data/JPEGImages/%s.jpg'%(image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

