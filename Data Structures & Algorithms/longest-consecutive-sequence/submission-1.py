class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns= set(nums)
        max_length = 0
        for i in ns:
            length = 0
            if i -  1  not in ns :
                while (i + length) in ns:
                    length = length + 1 
                max_length = max(length,max_length)
        return max_length