# Darrik Houck

import time
from math import floor
from random import random
import csv

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

# Partition for select_kth_2 and select_kth_3
def partition(arr, low, high):
  pivot = arr[high]
  i = (low - 1)
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
         
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return (i + 1)

# Different partition for select_kth_4
def partition_4(arr, pivot):
  left = 0
  right = len(arr) - 1
  i = 0

  while i <= right:
    if arr[i] == pivot:
      i += 1

    elif arr[i] < pivot:
      arr[left], arr[i] = arr[i], arr[left]
      left += 1
      i += 1
    else:
      arr[right], arr[i] = arr[i], arr[right]
      right -= 1

  return left

# Dividing list into sublists for select_kth_4
def chunks(arr, n):
  for i in range(0, len(arr), n):
    yield arr[i:i + n]

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
  split_arrs = chunks(arr, 5)

  sorted_arrs = [sorted(split_arr) for split_arr in split_arrs]
  medians = [sorted_arr[len(sorted_arr) // 2] for sorted_arr in sorted_arrs]

  if len(medians) <= 5:
    pivot_value = sorted(medians)[len(medians) // 2]
  else:
    pivot_value = select_kth_4(medians, len(medians) // 2)

  pivot = partition_4(arr, pivot_value)
  if k - 1 == pivot:
    return pivot_value
  elif k-1 < pivot:
    return select_kth_4(arr[:pivot], k)
  else:
    return select_kth_4(arr[pivot+1:], k-pivot-1)

def main():
  # Modify only these values to change how the program runs
  sizes = [10, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000, 10000]  # Number of elements
  kth = [1/4, 1/2, 3/4] # kth will always include 1st element and last element
  runs = 10

  for n in sizes:
    alg1_time, alg2_time, alg3_time, alg4_time = 0, 0, 0, 0

    # [1, n/4, n/2, 3n/4, n] with default kth list [1/4, 1/2, 3/4]
    indices = [1]
    indices.extend([floor(n*pos) for pos in kth])
    indices.append(n)

    for k in indices:
      for run in range(runs):
        print(f'run: {run+1}')
        print(f'k: {k}')
        test_list = [floor(random()*n) for x in range(n)] # n elements, random numbers from 0 to n-1

        list_dupe = test_list.copy()
        start_time = time.time()
        select_kth_1(list_dupe)
        list_dupe[k-1]  # Access time included (miniscule, but necessary for fair results)
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg1_time += time_elapsed

        list_dupe = test_list.copy()
        start_time = time.time()
        select_kth_2(list_dupe, 0, len(list_dupe)-1, k)
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg2_time += time_elapsed

        list_dupe = test_list.copy()
        start_time = time.time()
        select_kth_3(list_dupe, 0, len(list_dupe)-1, k)
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg3_time += time_elapsed

        list_dupe = test_list.copy()
        start_time = time.time()
        select_kth_4(list_dupe, k)
        end_time = time.time()
        time_elapsed = end_time - start_time
        alg4_time += time_elapsed
    with open('algorithm1.csv', 'a', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow([n, alg1_time/runs])
    with open('algorithm2.csv', 'a', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow([n, alg2_time/runs])
    with open('algorithm3.csv', 'a', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow([n, alg3_time/runs])
    with open('algorithm4.csv', 'a', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow([n, alg4_time/runs])

if __name__ == '__main__':
  main()