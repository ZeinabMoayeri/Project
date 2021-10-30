# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:58:59 2021

@author: zmoay
"""


from matplotlib import pyplot as plt
import random 
# Add your code below:
numbers_a = range(1, 11)
numbers_b = random.sample(range(1000), 10)
# print(numbers_b)
plt.plot(numbers_a, numbers_b)
plt.show()