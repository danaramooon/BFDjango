def make_chocolate(small, big, goal):
  if goal >= 5 * big:
    rd = goal - 5 * big
  else:
    rd = goal % 5
  if rd <= small:
    return rd
  return -1
