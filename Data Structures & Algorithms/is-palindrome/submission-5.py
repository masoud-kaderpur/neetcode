class Solution:
    def isPalindrome(self, s: string) -> bool:
        if len(s) == 0:
            return true
        
        s = s.lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.is_alphanumeric(s[l]):
                l += 1
            while l < r and not self.is_alphanumeric(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True			

    def is_alphanumeric(self, c) -> bool:
        return 	(ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('0') and ord(c) <= ord('9'))
