class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) < 3:
            return 0
        minimum = float("inf")
        maximum = 0
        average = 0
        for i in salary:
            minimum = min(minimum, i)
            maximum = max(maximum, i)
            average += i
        
        average -= minimum
        average -= maximum
        return average / (len(salary) - 2)
            
        