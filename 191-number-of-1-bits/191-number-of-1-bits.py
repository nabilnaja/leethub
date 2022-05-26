class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(b) for b in list(bin(n))[2:]])
    
        