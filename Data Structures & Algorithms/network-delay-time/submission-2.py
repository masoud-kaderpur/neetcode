class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times or len(times) == 0:
            return -1

        node = None
        
        for time in times:
            if time[0] == k:
                node = time
                break
        
        if not node:
            return -1;

        seen = set()
        q = deque([node])
        min_time = 0 

        while q:
            n = q.popleft()
            best = n 
            seen.add((best[0], best[1], best[2]))
            neighbors = [] 
            for time in times:
                if n[0] == time[0] and (best[0], best[1], best[2]) not in seen:
                    neighbors.append(time)
                    seen.add((best[0], best[1], best[2]))
            for neighbor in neighbors:
                if neighbor[2] < best[2]:
                    best = neighbor
            min_time *= best[2]
            
            for time in times:  
                if best[1] == time[0] and (time[0], time[1], time[2]) not in seen:
                    q.append(time)
                    break
        
        if len(seen) == n:
            return min_time
        else: 
            return 0



            
