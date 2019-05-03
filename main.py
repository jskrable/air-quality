#!/usr/bin/env python3
# coding: utf-8
"""
main.py
05-03-19
jack skrable
"""

print('Importing modules...')
# Libs
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import RobustScaler

print('Import complete')

print('Reading file...')
df = pd.read_csv('./data/pollution_us_2000_2016.csv')
print('Read complete')
print('Cleaning data...')
df.drop(df.select_dtypes(['object']), inplace=True, axis=1)
df.fillna(0, inplace=True)
print('Clean complete')

sns.heatmap(df.corr(), cmap="YlGnBu")