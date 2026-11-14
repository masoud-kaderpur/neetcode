class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        m = {}
        
        for num in nums:
            if num - 1 not in m:
                m[num] = 1
            else:
                m[num] = 1 + m.get(num - 1)

        return max(m.values())
