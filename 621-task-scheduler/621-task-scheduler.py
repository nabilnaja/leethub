class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time complexity: O(k) k is the len of tasks  
        Space complexity:  O(k)        
        """
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        frequencies.sort()
        
        f_max = frequencies.pop() - 1
        idle_time = f_max * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max, frequencies.pop())
        idle_time = max(0, idle_time)
        return idle_time + len(tasks)   
        
        