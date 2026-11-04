class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) 
        postfix = [1] * len(nums)
        result = [1] * len(nums)
        prefixV = 1
        postfixV = 1
        for i in range(len(nums)):
            prefixV *= nums[i]
            prefix[i] = prefixV 
        for i in reversed(range(len(nums))):
            postfixV *= nums[i]
            postfix[i] = postfixV
        i = 1
        j = len(nums) - 1 
        # result[0] = postfix[0]
        for i in range (len(nums)):
            pre = prefix[i - 1] if i > 0 else 1
            post = postfix[i + 1] if i < len(nums) - 1 else 1
            result[i] = pre * post
        return result