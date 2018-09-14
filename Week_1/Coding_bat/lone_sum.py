def lone_sum(a, b, c):
  if(a == b != c):
    return c
  elif(a == c != b):
    return b
  elif(b == c != a):
    return a
  elif(a == b == c):
    return 0
  return a+b+c