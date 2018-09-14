def caught_speeding(speed, is_birthday):
  if(is_birthday == True):
    if(speed <= 65):
      return 0
    if(66<=speed<=85):
      return 1
    if(86<=speed):
      return 2
  else:
    if(speed <= 60):
      return 0
    if(61<=speed<=80):
      return 1
    if(81<=speed):
      return 2
