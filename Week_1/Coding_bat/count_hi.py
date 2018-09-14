def count_hi(str):
  cnt = 0
  for i in range (0,len(str)-1):
    if(str[i]+str[i+1] == "hi"):
      cnt += 1
  return cnt
