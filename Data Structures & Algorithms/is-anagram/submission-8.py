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
        
        # sorted with O(n log n) time and O(n) space
        s = sorted(s); # O(n log n)
        t = sorted(t); # O(1)

        return s == t
        

        