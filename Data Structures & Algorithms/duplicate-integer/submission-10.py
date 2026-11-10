class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force approach with O(n^2) time complexity and O(1) space complexity 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False   
        
        # hashset approach 
        seen = set();
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False