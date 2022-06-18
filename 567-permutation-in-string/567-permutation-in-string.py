class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        ord_a = ord('a')
        s1_count, s2_count = [0] * 26, [0] * 26
        criteria_number = 0
        valid_criteria_number = 0

        for i in range(len(s1)):
            ch1 = ord(s1[i]) - ord_a
            ch2 = ord(s2[i]) - ord_a
            if not s1_count[ch1]:
                criteria_number += 1

            s1_count[ch1] += 1
            s2_count[ord(s2[i]) - ord_a] += 1

        for i in range(len(s1_count)):
            if s1_count[i] and s2_count[i] >= s1_count[i]:
                valid_criteria_number += 1

        if valid_criteria_number == criteria_number:
            return True

        l = 0
        for r in range(len(s1), len(s2)):

            ch_r = ord(s2[r]) - ord_a
            ch_l = ord(s2[l]) - ord_a

            s2_count[ch_r] += 1
            s2_count[ch_l] -= 1

            if s1_count[ch_r] and s2_count[ch_r] == s1_count[ch_r]:
                valid_criteria_number += 1
            if s1_count[ch_l] and s2_count[ch_l] == s1_count[ch_l] - 1:
                valid_criteria_number -= 1
            if s2_count == s1_count:
                return True

            l += 1

        return False