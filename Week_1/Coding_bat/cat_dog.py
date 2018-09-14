def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(0,len(str)-2):
    if(str[i] + str[i+1] + str[i+2] == "cat"):
      cat += 1
    if(str[i] + str[i+1] + str[i+2] == "dog"):
      dog += 1
  return dog == cat
