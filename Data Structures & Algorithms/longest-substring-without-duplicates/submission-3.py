class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        seen = deque()
        l = 0 # 2 
        # vdf 
        for c in s:   
            if c in seen:
                while c in seen:
                    seen.popleft()
            else:
                seen.append(c)
                l += 1
            l = max(l, len(seen))
        return ll	

                