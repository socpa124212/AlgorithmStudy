def count_sort(ary):
  count = [0]*(max(ary)+1)
  
  for i in range(len(ary)):
    count[ary[i]] =+ 1
  
  for i in range(len(count)):
    for j in range(count[i]):
      print(i, end = ' ')