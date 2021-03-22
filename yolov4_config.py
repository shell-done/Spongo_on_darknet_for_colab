# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:41:08 2020

@author: Quang Nguyen
"""

""" 
Generating custom cfg/yolov4_custom_train.cfg
and cfg/yolov4_custom_test.cfg

"""

classes=4
max_batches=8000
batch=64
subdivisions=32
width=832
height=704
channels=3
momentum=0.949
decay=0.0005
learning_rate=0.001
steps=(6400,7200)
scales=(0.1,0.1)

with open("data/classes.names") as f:
  lines = [l for l in f.readlines() if len(l) > 2 ]
  classes = len(lines)
  max_batches = 2000*classes
  steps = (int(0.8*max_batches), int(0.9*max_batches))

  print("Parameters changed :")
  print("classes : %d" % classes)
  print("max_batches : %d" % max_batches)
  print("steps : (%d,%d)" % steps)
