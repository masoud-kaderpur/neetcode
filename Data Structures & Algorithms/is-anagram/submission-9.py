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

        # sorted with O(n log n) time and O(1) space
        # s = sorted(s); # O(n log n) time and O(1) space
        # t = sorted(t); # O(n log n) time and O(1) space
        # return s == t

        # hashmap with O(n) time and O(n) space
        mapS, mapT = {}, {} 
        for i in range(len(s)): # O(n) time
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        return mapS == mapT
