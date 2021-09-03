# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:09:32 2021

@author: zmoay
"""
radius = float(input('Enter a radius : '))
height = float(input('Enter a height : '))
print('Volume is :', (22/7) * radius * radius * height)
print('Area is :',  ((22/7) * radius * 2 * height)+
 (2 * ((22/7) * radius ** 2)))