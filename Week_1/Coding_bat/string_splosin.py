def string_splosion(str):
  s = ""
  for i in range (0, len(str)):
    s += str[:i+1]
  return s
