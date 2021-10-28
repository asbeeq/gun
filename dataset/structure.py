#!/bin/bash

from random import random
import os
from glob import glob, escape
import json


image_paths = glob("Images/*")
annotation_file = 'gun.json'
annotations = json.load(open(annotation_file))

cleaned_annotations = {}
for k,v in annotations['_via_img_metadata'].items():
    cleaned_annotations[v['filename']] = v

train_annotations = {}
valid_annotations = {}
for img in image_paths:
    if random()<0.2:
        os.system("cp "+ img + " procdata/val/")
        img = img.split("/")[-1]
        valid_annotations[img] = cleaned_annotations[img]
    else:
        os.system("cp "+ img + " procdata/train/")
        img = img.split("/")[-1]
        train_annotations[img] = cleaned_annotations[img]

with open('procdata/val/gun.json', 'w') as fp:
    json.dump(valid_annotations, fp)
with open('procdata/train/gun.json', 'w') as fp:
    json.dump(train_annotations, fp)