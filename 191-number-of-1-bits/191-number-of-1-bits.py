class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_value = bin(n)
        return sum([int(bin_value[i]) for i in range(2, len(bin_value))])
    
        