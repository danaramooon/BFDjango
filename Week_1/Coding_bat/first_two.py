def first_two(str):
  s = ""
  if(len(str) >= 2):
    for i in range (0, 2):
       s += str[i]
    return s
  else:
    return str
  

