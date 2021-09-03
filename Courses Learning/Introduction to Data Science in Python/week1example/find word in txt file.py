# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:20:07 2021

@author: zmoay
"""

import re
import sys
import os

pattern = re.compile("Hello")

for line in open("ss.txt"):
    for match in re.finditer(pattern, line):
        print(line)