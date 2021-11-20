# Darrik Houck

import time
from math import floor
import numpy as np
from numpy.lib.function_base import median, select

# Helper functions
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

def partition(arr, low, high):
  pivot = arr[high]
  i = (low - 1)
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
         
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return (i + 1)

def chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

# Algorithm 1: Merge Sort
def select_kth_1(list):
  length = len(list)
  if length <= 1: return

  mid = length // 2
  left = list[:mid]
  right = list[mid:]

  select_kth_1(left)
  select_kth_1(right)
  merge(list, left, right)

# Algorithm 2: Iterative QuickSelect
def select_kth_2(arr, low, high, k):
  while low <= high:
    pivot = partition(arr, low, high)
    if pivot == k - 1:
      return arr[pivot]
    elif pivot > k - 1:
      high = pivot - 1
    else:
      low = pivot + 1

  return -1

# Algorithm 3: Recursive QuickSelect
def select_kth_3(arr, low, high, k):
  if low > high: return -1

  pivot = partition(arr, low, high)
  if pivot == k - 1:
    return arr[pivot]
  elif pivot > k - 1:
    return select_kth_3(arr, low, pivot-1, k)
  else:
    return select_kth_3(arr, pivot+1, high, k)

# Algorithm 4: QuickSelect with Median of Medians
def select_kth_4(arr, k):
  # Split arr into separate lists of 5 elements
  split_arrs = list(chunks(arr, 5))

  # Disgusting list comprehension
    # First sorts all lists in splits_arrs,
    # then appends middle index to medians
  medians = [sorted(split_arr)[len(split_arr)//2] for split_arr in split_arrs]

  if len(medians) <= 5:
    pivot_value = sorted(medians)[len(medians)//2]
  else:
    pivot_value = select_kth_4(medians, len(medians)//2)

  low = [j for j in arr if j < pivot_value]
  high = [j for j in arr if j > pivot_value]

  pivot = len(low)
  if k - 1 < pivot:
    return select_kth_4(low, k)
  elif k - 1 > pivot:
    return select_kth_4(high, k-pivot-1)
  else:
    return pivot_value

def main():
  sizes = [10]
  kth = [1/4, 1/2, 3/4]
  runs = 10

  for n in sizes:
    alg1, alg2, alg3, alg4 = 0, 0, 0, 0

    k = [1]
    k.extend([floor(n*pos) for pos in kth])
    k.append(n)

    for index in k:
      for run in range(runs):
        print(f'run: {run}')
        print(f'k: {index}')
        test_list = [x for x in range(n)]

        print('Algorithm 1: Merge Sort')
        # Avoid sorting row by creating copy
        list_dupe = test_list.copy()
        start_time = time.time()
        select_kth_1(list_dupe)
        print(list_dupe[index])
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg1 += time_elapsed

        print('Algorithm 2: Iterative QuickSearch')
        list_dupe = test_list.copy()
        start_time = time.time()
        print(select_kth_2(list_dupe, 0, len(list_dupe)-1, index))
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg2 += time_elapsed

        print('Algorithm 3: Recursive QuickSearch')
        list_dupe = test_list.copy()
        start_time = time.time()
        print(select_kth_3(list_dupe, 0, len(list_dupe)-1, index))
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg3 += time_elapsed

        print('Algorithm 4: QuickSearch with Median of Medians')
        list_dupe = test_list.copy()
        start_time = time.time()
        print(select_kth_4(list_dupe, index))
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg4 += time_elapsed

if __name__ == '__main__':
  main()