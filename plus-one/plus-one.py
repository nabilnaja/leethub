class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rest, i = 1, len(digits) - 1
        while rest and i >= 0:
            rest = digits[i] == 9
            digits[i] = 0 if rest else digits[i] + 1
            i -= 1
        if rest:
            digits.insert(0,1)
        return digits
            
            
            
        