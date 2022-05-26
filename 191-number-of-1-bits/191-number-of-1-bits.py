class Solution:
    def hammingWeight(self, n: int) -> int:
        return reduce(lambda x,y: int(x) + int(y), list(bin(n))[2:])
    
        