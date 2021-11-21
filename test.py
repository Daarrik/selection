from math import floor
from random import random
import numpy as np

def merge(list, left, right):
  i, j, k = 0, 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      list[k] = left[i]
      i += 1
    else:
      list[k] = right[j]
      j += 1
    k += 1
  
  while i < len(left):
    list[k] = left[i]
    i += 1
    k += 1
  
  while j < len(right):
    list[k] = right[j]
    j += 1
    k += 1

def select_kth_1(list):
  length = len(list)
  if length <= 1: return

  mid = length // 2
  left = list[:mid]
  right = list[mid:]

  select_kth_1(left)
  select_kth_1(right)
  merge(list, left, right)

# def mergeSort(arr):
#     if len(arr) > 1:
  
#          # Finding the mid of the array
#         mid = len(arr)//2
  
#         # Dividing the array elements
#         L = arr[:mid]
  
#         # into 2 halves
#         R = arr[mid:]
  
#         # Sorting the first half
#         mergeSort(L)
  
#         # Sorting the second half
#         mergeSort(R)
  
#         i = j = k = 0
  
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
  
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
  
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

# test_list = np.random.randint(low=0, high=10, size=10)
test_list = [floor(random()*10+1) for x in range(10)]
# test_list = [6, 3, 4, 4, 1, 2, 2, 7]
dupe_list = test_list.copy()
print(dupe_list)
print(test_list)
select_kth_1(dupe_list)
print(test_list)
print(dupe_list)