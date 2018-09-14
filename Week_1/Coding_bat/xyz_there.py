def xyz_there(str):
  if(str.startswith("xyz")):
    return True
  if("." in str):
    for i in range (str.find(".") + 2, len(str)-2):
      if(str[i] + str[i+1]+str[i+2] == "xyz" and str[i-1] != "."):
        return True
  else:
    if("xyz" in str):
      return True
  return False
    
