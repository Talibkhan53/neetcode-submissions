class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        i = 0 
        j = len(nums) - 1 
        while i < j :
            sum = nums[i] + nums[j]
            if sum > target:
                j = j - 1
            elif sum < target:
                i = i + 1
            else:
                l.append(i+1)
                l.append(j+1)
                return l
                

          
        