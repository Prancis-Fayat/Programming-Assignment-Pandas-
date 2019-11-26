# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:22:52 2019

@author: Prancis Fayat
"""

import pandas as pd

cars = pd.read_csv('C:\\Users\\Prancis Fayat\\Desktop\\python scripts\\prog assignment pandas\\cars.csv')
a = cars.iloc[ :,1::2].head()
b = cars.loc[cars['Model'] == "Mazda RX4", ]
c = cars.loc[cars["Model"] == "Camaro Z28", "cyl"]
d = cars.loc[[0,28,18], ["Model","cyl", "gear"]]
