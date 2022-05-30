class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT


        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor


        max_bit = 0
        while divisor >= HALF_MIN_INT and divisor + divisor >= dividend:
            max_bit += 1
            divisor += divisor

        quotient = 0
        for bit in range(max_bit, -1, -1):
            if divisor >= dividend:
                quotient -= (1 << bit)
                dividend -= divisor
            divisor = (divisor + 1) >> 1

        return -quotient if negatives != 1 else quotient
