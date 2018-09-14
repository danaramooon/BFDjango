def string_bits(str):
  s = ""
  for i in range (0,len(str)):
    if(i%2 == 0):
      s += str[i]
  return s
  
