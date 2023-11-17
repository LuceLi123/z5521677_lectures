""" lec_pd_series.py

Companion codes for the lecture on pandas Series
"""

import pandas as pd


# ---------------------------------------------------------------------------- 
#   The dates and prices lists
# ---------------------------------------------------------------------------- 
dates = [
  '2020-01-02', 
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600, 
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# ---------------------------------------------------------------------------- 
#   Create a Series instance
# ---------------------------------------------------------------------------- 
# Create a series object
ser  = pd.Series(data=prices, index=dates)
print(ser)

# Select Qantas price on '2020-01-02' ($7.16) using ...

# ... the `prices` list
prc0  = prices[dates.index('2020-01-02')]
print(prc0)

# ... the `ser` series
prc1  = ser['2020-01-02']
print(prc1)

# ---------------------------------------------------------------------------- 
#   Slicing series
# ---------------------------------------------------------------------------- 
# Unlike dictionaries, you can slice a series
prcs  = ser['2020-01-06':'2020-01-10'] # Do not need to +1 since using series
print(prcs)

# prices[dates.index('2020-01-06'):dates.index('2020-01-10')+1] # Use lists to slice

# ---------------------------------------------------------------------------- 
#   Accessing the underlying array
# ---------------------------------------------------------------------------- 

# Use `.array` to get the underlying data array
ary  = ser.array
print(ary)

# Like any instance, you can get its type (i.e., the class used to create the
# instance)
print(type(ser.array))

# Use the `index` attribute to get the index from a series
the_index  = ser.index
print(the_index)

x = ser[1000]
x = prices[1000] # Out of range error since do not have many elements
print(x)

# Like any instance, you can get its type (i.e., the class used to create the
# instance).
print('The type of `the_index` is', type(the_index))

# ---------------------------------------------------------------------------- 
#   Changing the index by assignment
# ---------------------------------------------------------------------------- 

# The old index is:
#
Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
       '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
      dtype='object')

# Replace the existing index with another with different values
# Note the -4 and 1000  
ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000]

# The new index is:
Int64Index([0, 1, 2, 3, -4, 5, 6, 7, 8, 1000], dtype='int64')

chara = ['a', 'b', 'c']
num = ['1', '2', '3']

series_abc = pd.Series(data=num, index=chara)

# ---------------------------------------------------------------------------- 
#   Selecting obs using the new index
# ---------------------------------------------------------------------------- 
# Lets see how the series looks like
#print(ser) 

# This will return 7.04
x  = '?'
#print(x) 

# Compare the following cases:
# 1. This will return the element associated with the index label -4 
#    (or 6.86)
#print(ser[-4]) 

# 2. This will return the fourth element from the end of the **list** `prices` 
#    (or 7.00)
#print(prices[-4])


prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
pseries_stk = pd.Series(data=prc_date.values(), index=prc_date.keys())  #  Unpack dic in Series

dic = {i:i+1 for i in range(10000)}
series_ones = pd.Series(data=1, index=dic.keys())

prc, date = list(prc_date.keys()), list(prc_date.values())
prc = [int(prc) for i in prc]
date = [int(date) for i in date]


