def count_code(str):
  cnt = 0
  for i in range (0,len(str)-3):
    if(str[i]+str[i+1]+str[i+3] == "coe"):
      cnt += 1
  return cnt

