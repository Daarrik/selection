from math import floor
import numpy as np
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

def select_kth_3(arr, low, high, k):
  if low > high: return -1

  pivot = partition(arr, low, high)
  if pivot == k - 1:
    return arr[pivot]
  elif pivot > k - 1:
    return select_kth_3(arr, low, pivot-1, k)
  else:
    return select_kth_3(arr, pivot+1, high, k)
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

n = 10
kth = [1/4, 1/2, 3/4]
k = [1]
k.extend(floor(n*index) for index in kth)
k.append(n)
print(k)

test_list = [1,1,1,1,1,1,1,1,1]
# print(test_list)
# print(sorted(test_list))
# for index in k:
#   print(f'index:{index}')
#   list_dupe = test_list.copy()
#   print(test_list)
#   print(list_dupe)
print(select_kth_3(test_list, 0, len(test_list)-1, 8))