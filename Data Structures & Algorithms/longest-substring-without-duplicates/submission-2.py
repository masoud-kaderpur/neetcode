class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        seen = set()
        ll = 0 
        l = 0
        # abcabcbb
        for c in s:   
            if c in seen:
                seen.clear()
                seen.add(c)
                l = 1
            else:
                seen.add(c)
                l += 1
            if l > ll:
                ll = l
        return ll	

                