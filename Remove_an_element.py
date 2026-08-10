# 27. Remove an Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return i
            
          
       
                
            
           
            

            
        