# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:53:34 2016

@author: Bluefish_
"""

import numpy.random as rand
import numpy as np

mean = int(input("Please enter the average score: "))
stddev = int(input("Please enter the standard deviation: "))
size = int(input("Please enter the size of the class: "))

distribution = np.sort(rand.normal(mean, stddev, size))

score = int(input("Please enter your score for this test: "))
rank = []

for j in range(1000):
    for i in range(size):
        if score<=distribution[i]:
            rank.append(size-i)
            break;
            
ranking = max(rank,key = rank.count)
print("Your estimated ranking is {}/{}.\n".format(str(ranking),str(size)))
            