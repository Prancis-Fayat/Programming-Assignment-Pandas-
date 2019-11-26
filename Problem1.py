# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:42:06 2019

@author: Prancis Fayat
"""

import pandas as pd

cars = pd.read_csv('C:\\Users\\Prancis Fayat\\Desktop\\python scripts\\prog assignment pandas\\cars.csv')
a = cars.head()
b = cars.tail()
print('first five rows: \n', a)
print('last five rows: \n', b)