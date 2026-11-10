class Solution:
    # lower and upper bounds: 
    #   lower bounds: N >= 0
    #   upper bounds: N <= 10^5
    # extreme edges: 
    #   N = 0, N = 1 
    #   the first two are the same
    #   all unique
    #   late duplicate

    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force approach with O(n^2) time and O(1) space 
        # for i in range(len(nums)): # O(n) time 
        #     for j in range(i + 1, len(nums)): # O(n) time 
        #         if nums[i] == nums[j]: # O(1) time
        #             return True 
        # return False 

        # hashset approach with O(n) time and space 
        seen = set() # O(1) time and space
        for n in nums: # O(n) time
            if n in seen: # O(1) time 
                return True  
            seen.add(n)  # O(1) time
        return False  
