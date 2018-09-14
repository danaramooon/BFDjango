def max_end3(nums):
  a = []
  for i in range(3):
    a.append(max(nums[0],nums[len(nums)-1]))
  return a
