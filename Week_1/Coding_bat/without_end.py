def without_end(str):
  s = ""
  if(len(str) > 2):
    for i in range(1,len(str)-1):
      s += str[i]
    return s
  else:
    return ""
