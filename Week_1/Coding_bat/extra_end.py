def extra_end(str):
  s = ""
  if(len(str) >= 3):
    for i in range (len(str)-2, len(str)):
       s += str[i]
    return s * 3
  else:
    return str * 3
  
