def quick_sort(arr):
  if len(arr)<=1:
    return arr
  
  pivot = arr[0]
  tail = arr[1:]

  left_side = [x for x in tail if x < pivot]
  right_side = [x for x in tail if x >= pivot]

  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

array = [5, 7, 9, 0, 3, 9, 6, 2, 4, 8]

print(quick_sort(array))