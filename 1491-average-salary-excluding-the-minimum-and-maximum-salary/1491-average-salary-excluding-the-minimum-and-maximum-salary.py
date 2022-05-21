class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) < 3:
            return 0
        minimum = min(salary)
        maximum = max(salary)
        average = sum(salary) - minimum - maximum  
        
        return average / (len(salary) - 2)
            
        