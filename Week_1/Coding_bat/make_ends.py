def make_ends(nums):
  a = []
  if(len(nums)==1):
    a.append(nums[0])
    a.append(nums[0])
  if(len(nums)>1):
    a.append(nums[0])
    a.append(nums[len(nums)-1])
  return a
