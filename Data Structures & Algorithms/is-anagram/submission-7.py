# lower and upper bounds:
#   lower bounds: N, M >= 1
#   upper bounds: N, M <= 5 * 10^4
# edge cases:
#   N, M == 1
#   either N or M is longer then the other 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        s = sorted(s);
        t = sorted(t);
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

        