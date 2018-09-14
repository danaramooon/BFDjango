def front3(str):
  s = ""
  if(len(str) >= 3):
    for i in range (0, 3):
       s += str[i]
    return s * 3
  else:
    return str * 3
  