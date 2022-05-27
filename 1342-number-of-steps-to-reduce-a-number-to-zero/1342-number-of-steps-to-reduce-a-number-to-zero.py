class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 1:
            return num
        return self.numberOfSteps(num >> 1) + 1 if num % 2 == 0 else self.numberOfSteps((num -1 ) >> 1) + 2
        