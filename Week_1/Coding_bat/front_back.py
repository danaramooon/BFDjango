def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
def front_back(str):
  if(len(str)<2):
    return str
  return swap(str,0,len(str)-1)
