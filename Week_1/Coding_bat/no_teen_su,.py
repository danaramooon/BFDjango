def no_teen_sum(a, b, c):
  if(13<=a<=14 or 17<=a<=19):
    a = 0
  if(13<=b<=14 or 17<=b<=19):
    b = 0
  if(13<=c<=14 or 17<=c<=19):
    c = 0
  return a + b + c
