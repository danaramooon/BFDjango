def near_ten(num):
  if(num % 10 <= 2 or (num+1)%10 == 0 or (num + 2)%10 == 0):
    return True
  return False
