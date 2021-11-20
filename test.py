from math import floor
import numpy as np

def chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

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

test_list = np.random.randint(low=0, high=n, size=n)
print(test_list)
print(sorted(test_list))
for index in k:
  print(f'index:{index}')
  list_dupe = test_list.copy()
  print(test_list)
  print(list_dupe)
  print(select_kth_4(list_dupe, index))