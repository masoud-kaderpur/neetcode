class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Frequency count map
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # 2. Inverted map: frequency -> list of numbers with that frequency
        # Using a list prevents collisions when multiple numbers share a count
        arr = {}
        for n, c in count.items():
            if c not in arr:
                arr[c] = []
            arr[c].append(n)

        # 3. Collect from highest frequency down to lowest
        l = []
        for c in sorted(arr.keys(), reverse=True):
            for num in arr[c]:
                l.append(num)
                if len(l) == k:
                    return l

        return l
