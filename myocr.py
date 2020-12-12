# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:39:02 2020

@author: ub226
"""

import easyocr # To install run the following in your terminal - pip install easyocr
import csv

reader = easyocr.Reader(['en'])


################################## HYPERPARAMETERS ############################
path_to_image = "./test_images/datanam.jpg"
one_line_space = 80
###############################################################################


def preprocess():
    results = reader.readtext(path_to_image)
    bboxes = []
    coord = []
    diff = []
    text = []
    ans = []
    for item in results:
        a, b, _ = item
        bboxes.append(a)
        text.append(b)
    for item in bboxes:
        _, _, _, d = item
        _, b = d
        coord.append(b)
    for i in range (1, len(coord)):
        diff.append(coord[i]-coord[i-1])    
    print(diff)
    for i in range(len(text)):
        ans.append(text[i])
        if i==(len(text)-1):
            continue
        n = int(diff[i]/one_line_space)
        for i in range (n):
            ans.append(" ")
    with open("output.csv", 'w') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(ans)
    return ans

ans = preprocess()

for item in ans:
    print(item)