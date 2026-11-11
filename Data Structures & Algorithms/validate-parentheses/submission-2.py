class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        for c in s:
            if c == ")":
                if len(queue) == 0 or queue.pop() != "(":
                    return False
            elif c == "}":
                if len(queue) == 0 or queue.pop() != "{":
                    return False
            elif c == "]":
                if len(queue) == 0 or queue.pop() != "[":
                    return False
            else:
                queue.append(c)
        return True
