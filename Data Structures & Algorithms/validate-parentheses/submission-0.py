class Solution:
    def isValid(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            match s[l]:
                case '(':
                    if s[r] != ')':
                        return False
                case '{':
                    if s[r] != '}':
                        return False
                case '[':
                    if s[r] != ']':
                        return False
            l, r = l + 1, r - 1
        
        return True