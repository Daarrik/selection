from math import floor
from random import random
  
def chunks(arr, n):
  for i in range(0, len(arr), n):
    yield arr[i:i + n]

data = [1,2,3,4,5,6,7,8,9,10]
split = chunks(data, 5)
for arr in split:
  print(arr)