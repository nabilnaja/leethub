class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        
        if len(s2) < len(s1):
            return False

        ord_a = ord('a')
        size_count = criteria_number = 26
        s1_count, s2_count = [0] * size_count, [0] * size_count
        valid_criteria_number = 0

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord_a] += 1
            s2_count[ord(s2[i]) - ord_a] += 1

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                valid_criteria_number += 1

        l = 0

        for r in range(len(s1), len(s2)):

            if valid_criteria_number == criteria_number:
                return True

            ch_l, ch_r = ord(s2[l]) - ord_a, ord(s2[r]) - ord_a

            s2_count[ch_r] += 1

            if s2_count[ch_r] == s1_count[ch_r]:
                valid_criteria_number += 1
            elif s2_count[ch_r] == s1_count[ch_r] + 1:
                valid_criteria_number -= 1

            s2_count[ch_l] -= 1

            if s2_count[ch_l] == s1_count[ch_l]:
                valid_criteria_number += 1
            elif s2_count[ch_l] == s1_count[ch_l] - 1:
                valid_criteria_number -= 1
            l += 1

        return valid_criteria_number == criteria_number