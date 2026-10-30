class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        i = 0
        while i < k:
            temp = max(d,key=d.get)
            l.append(temp)
            del d[temp]
            i = i + 1
        return l
            

        