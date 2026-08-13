# 977. Sqaures of a Sorted Array
class Solution:
  def sortedSq(self, nums:List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    for i in range(len(nums)):
      if abs(nums[left]) > abs(nums[right]):
        result[i] = nums[left] * nums[left]
        left += 1
      else:
        result[i] = nums[right] * nums[left]
        right -= 1
    
