def string_match(a, b):
  mim = min(len(a), len(b))
  cnt = 0
  for i in range(0,mim-1):
    s1 = a[i:i+2]
    s2= b[i:i+2]
    if (s1 == s2):
      cnt += 1
  return cnt